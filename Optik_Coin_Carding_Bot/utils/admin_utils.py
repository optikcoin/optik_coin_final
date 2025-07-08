def is_admin(user_id, admin_ids):
    """
    Check if a user ID is in the list of admin IDs.
    """
    return user_id in admin_ids

def format_user_list(users):
    """
    Format a list of user tuples for display.
    Each user tuple should be (id, username, balance).
    """
    if not users:
        return "No users found."
    return "\n".join([f"{u[1]} (Balance: {u[2]})" for u in users])