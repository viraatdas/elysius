from pysnark.runtime import snark, IfElse, PubVal

# Define eligible voters as public values to be used in conditional checks
eligible_voters = [PubVal(123456), PubVal(234567), PubVal(345678)]  # Example eligible IDs

@snark
def is_eligible(voter_id):
    # Check if voter_id matches any value in eligible_voters
    return IfElse(voter_id == eligible_voters[0], 1,
                  IfElse(voter_id == eligible_voters[1], 1,
                         IfElse(voter_id == eligible_voters[2], 1, 0)))

# Example usage
voter_id = PubVal(123)  # Use a public value for the voter_id to check eligibility
print("Voter eligibility:", is_eligible(voter_id).val())

