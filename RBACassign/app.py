# Hardcoded users with roles
users = {
    "bryan_admin": "admin",
    "bryan_user": "user"
}

# Simulated login
current_username = "bryan_user"
current_role = users[current_username]

print(f"Logged in as: {current_username}")
print(f"Role: {current_role}")
print("-" * 30)

# Admin only action


def admin_panel():
    if current_role == "admin":
        print("Access granted: Welcome to the admin panel.")
    else:
        print("Access denied: Admins only.")

# User only action


def user_dashboard():
    if current_role == "user":
        print("Access granted: Welcome to the user dashboard. ")
    else:
        print("Access denied: Users only. ")


# Test both actions
admin_panel()
user_dashboard()

# This script demonstrates Confidentiality in the CIA triad.
# Confidentiality means only authorized users should access certain information or actions.
# In this app, role checks prevent admins and users from accessing each other's protected functions.
