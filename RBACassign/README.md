# RBAC Assignment

## Overview
This project is a very basic Python script that demonstrates authentication, user roles, and access control.

## How it works
- The script uses hardcoded usernames and roles.
- A login is simulated by setting the `current_username` variable.
- Two roles are used: `admin` and `user`.
- The app includes two protected functions:
  - `admin_panel()` can only be accessed by an admin
  - `user_dashboard()` can only be accessed by a user

## CIA Triad
This app demonstrates Confidentiality .

Confidentiality means making sure only authorized users can access certain information or actions. In this script, role checks are used to prevent one role from accessing functions meant for another role.

## How to run
Use this command in the terminal:

```bash
python3 app.py