# 10-Year Heart Attack Risk Estimator (NIH/Framingham point model)
#
# Paste a line like:
#   sex:M age:30 cho:120 smo:N hdl:60 sbp:100 med:N
# and get it back with the result appended:
#   sex:M age:30 cho:120 smo:N hdl:60 sbp:100 med:N out:<1

import sys

AGE_LIMITS = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]   # upper bounds (exclusive)
AGE_PTS = {
    "F": [-7, -3, 0, 3, 6, 8, 10, 12, 14, 16],
    "M": [-9, -4, 0, 3, 6, 8, 10, 11, 12, 13],
}

# Columns: age 20-39, 40-49, 50-59, 60-69, 70-79
# Rows: <160, 160-199, 200-239, 240-279, >=280
CHOL_PTS = {
    "F": [[0, 0, 0, 0, 0],
          [4, 3, 2, 1, 1],
          [8, 6, 4, 2, 1],
          [11, 8, 5, 3, 2],
          [13, 10, 7, 4, 2]],
    "M": [[0, 0, 0, 0, 0],
          [4, 3, 2, 1, 0],
          [7, 5, 3, 1, 0],
          [9, 6, 4, 2, 1],
          [11, 8, 5, 3, 1]],
}
SMOKER_PTS = {
    "F": [9, 7, 4, 2, 1],
    "M": [8, 5, 3, 1, 1],
}

# Rows: <120, 120-129, 130-139, 140-159, >=160 -> (untreated, treated)
BP_PTS = {
    "F": [(0, 0), (1, 3), (2, 4), (3, 5), (4, 6)],
    "M": [(0, 0), (0, 1), (1, 2), (1, 2), (2, 3)],
}

# Risk lookup: (minimum points, risk text), checked from highest to lowest
RISK_TABLE = {
    "F": [(25, ">=30"), (24, "27"), (23, "22"), (22, "17"), (21, "14"),
          (20, "11"), (19, "8"), (18, "6"), (17, "5"), (16, "4"),
          (15, "3"), (13, "2"), (9, "1")],
    "M": [(17, ">=30"), (16, "25"), (15, "20"), (14, "16"), (13, "12"),
          (12, "10"), (11, "8"), (10, "6"), (9, "5"), (8, "4"),
          (7, "3"), (5, "2"), (0, "1")],
}

REQUIRED_KEYS = ["sex", "age", "cho", "smo", "hdl", "sbp", "med"]


def age_points(sex, age):
    for limit, pts in zip(AGE_LIMITS, AGE_PTS[sex]):
        if age < limit:
            return pts


def age_group(age):
    return 0 if age < 40 else min((age - 40) // 10 + 1, 4)


def chol_row(chol):
    for i, limit in enumerate([160, 200, 240, 280]):
        if chol < limit:
            return i
    return 4


def hdl_points(hdl):
    if hdl >= 60: return -1
    if hdl >= 50: return 0
    if hdl >= 40: return 1
    return 2


def bp_row(sbp):
    for i, limit in enumerate([120, 130, 140, 160]):
        if sbp < limit:
            return i
    return 4


def lookup_risk(sex, total):
    for min_pts, risk in RISK_TABLE[sex]:
        if total >= min_pts:
            return risk
    return "<1"


def ten_year_risk(sex, age, total_chol, hdl, sbp, treated, smoker):
    """Returns (total_points, risk_string)."""
    g = age_group(age)
    total = age_points(sex, age)
    total += CHOL_PTS[sex][chol_row(total_chol)][g]
    total += SMOKER_PTS[sex][g] if smoker else 0
    total += hdl_points(hdl)
    total += BP_PTS[sex][bp_row(sbp)][1 if treated else 0]
    return total, lookup_risk(sex, total)


def parse_yes_no(value, name):
    v = value.strip().upper()
    if v not in ("Y", "N"):
        raise ValueError(f"{name} must be Y or N, got '{value}'")
    return v == "Y"


def parse_number(value, name, as_int=False):
    try:
        num = int(value) if as_int else float(value)
    except ValueError:
        raise ValueError(f"{name} must be a number, got '{value}'")
    if num < 0:
        raise ValueError(f"{name} cannot be negative")
    return num


def process_line(line):
    """Takes 'sex:M age:30 ...' and returns the same text with ' out:<risk>' added."""
    tokens = [t for t in line.split() if not t.lower().startswith("out:")]
    fields = {}
    for token in tokens:
        if ":" not in token:
            raise ValueError(f"'{token}' is not in key:value form")
        key, value = token.split(":", 1)
        fields[key.strip().lower()] = value.strip()

    missing = [k for k in REQUIRED_KEYS if k not in fields]
    if missing:
        raise ValueError("missing field(s): " + ", ".join(missing))

    sex = fields["sex"].upper()
    if sex not in ("M", "F"):
        raise ValueError(f"sex must be M or F, got '{fields['sex']}'")
    age = parse_number(fields["age"], "age", as_int=True)
    if not 20 <= age <= 79:
        raise ValueError("age must be 20-79 (the model does not cover other ages)")
    chol = parse_number(fields["cho"], "cho")
    hdl = parse_number(fields["hdl"], "hdl")
    sbp = parse_number(fields["sbp"], "sbp")
    smoker = parse_yes_no(fields["smo"], "smo")
    treated = parse_yes_no(fields["med"], "med")

    _, risk = ten_year_risk(sex, age, chol, hdl, sbp, treated, smoker)
    return " ".join(tokens) + " out:" + risk


def handle(line):
    try:
        print(process_line(line))
    except ValueError as err:
        print(line.strip() + " out:invalid")
        print(f"  ({err})", file=sys.stderr)


def main():
    # Optional: pass the string as a command-line argument
    if len(sys.argv) > 1:
        handle(" ".join(sys.argv[1:]))
        return

    print("Paste a line like: sex:M age:30 cho:120 smo:N hdl:60 sbp:100 med:N")
    print("(press Enter on a blank line to quit)")
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        if not line.strip():
            break
        handle(line)


if __name__ == "__main__":
    main()