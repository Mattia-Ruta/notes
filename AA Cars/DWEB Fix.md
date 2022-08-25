# Website Settings Not Setup Correctly

1. Go to DNA shell and run `dweb new group <group_id>`
2. Take note of the Group ID and the Site ID.. which is the <dweb_id>
3. Go to DNA's Database server and go to the `vcarsdms` database
4. Query vcarsdms.branch for the branch using the Group ID, take note of <branch_id>

UPDATE dweb_site SET branch_id = <branch_id> WHERE dweb_id = <dweb_id>;
