from main import clubHouseTracker

if __name__ == "__main__":


    # Initialize Main Class
    tracker = clubHouseTracker()


    # Create Hash Table
    tracker.initializeHash()


    # Insert Records in Table
    with open('inputPS8.txt') as f:
        a = f.read()
    rows = a.split('\n')
    for row in rows:
        values = [x.strip() for x in row.split('/')]
        tracker.insertAppDetails(*values)
    output_text = f"\nSuccessfully inserted {len(rows)} applications into the system."
    print(output_text)
    tracker._writeOutput(output_text)


    # Update Record in Table
    tracker.updateAppDetails('Deepak Prasad', '9923212234', status='Verified')


    # get list of applicants reffered by a member
    tracker.memRef('11129')


    # get list of applicants reffered by a member
    tracker.appStatus()

