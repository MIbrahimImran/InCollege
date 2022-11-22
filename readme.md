# Assumptions

1. All screen names should be unique!

# Folder structure

1. Services - To Make network requests or control databases
2. Shared - Contains all the folders that is required functionality by multiple files (Avoid code duplication)
3. Test - This is where all the test cases go
4. Models - To structure data in models, e.g users.
5. Constants - Anyting that is static, usualy contains booleans and strings.

# Populate Database

1. To populate the database use the command 'python development/create_mock_user_data.py' in the root directory

# Run Tests

1. In the root directory, run the command 'pytest -v test.py'

# Todo

- User can only delete the jobs they created!
