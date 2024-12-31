from pysnark.runtime import snark, PubVal
import csv

@snark
def verify_voter_eligibility(voter_id, district_id, is_eligible):
    # Convert inputs to public values
    pub_voter_id = PubVal(voter_id)
    pub_district_id = PubVal(district_id)
    pub_is_eligible = PubVal(is_eligible)
    
    # Your verification logic here
    # This is a simplified example
    return pub_is_eligible

def main():
    with open('mock_data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            voter_id = int(row['voter_id'])
            district_id = int(row['district_id'])
            is_eligible = row['is_eligible'].lower() == 'true'
            
            result = verify_voter_eligibility(voter_id, district_id, is_eligible)
            print(f"Voter {voter_id}: {'Eligible' if result else 'Not Eligible'}")

if __name__ == "__main__":
    main()