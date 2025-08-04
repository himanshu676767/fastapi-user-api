# import json
# import os
#
# class UserService:
#     def __init__(self):
#         self.file_path = "app/data/users.json"
#         if not os.path.exists(self.file_path):
#             with open(self.file_path, "w") as f:
#                 json.dump([], f)
#
#     def _read_data(self):
#         with open(self.file_path, "r") as f:
#             return json.load(f)
#
#     def _write_data(self, data):
#         with open(self.file_path, "w") as f:
#             json.dump(data, f, indent=2)
#
#     def create_user(self, user):
#         users = self._read_data()
#         user_id = len(users) + 1
#         new_user = {"id": user_id, **user.dict()}
#         users.append(new_user)
#         self._write_data(users)
#         return new_user
#
#     def get_users(self):
#         return self._read_data()
#
#     def get_user(self, user_id):
#         users = self._read_data()
#         return next((u for u in users if u["id"] == user_id), None)
#
#     def update_user(self, user_id, user):
#         users = self._read_data()
#         for u in users:
#             if u["id"] == user_id:
#                 u.update(user.dict())
#                 self._write_data(users)
#                 return u
#         return None
#
#     def delete_user(self, user_id):
#         users = self._read_data()
#         updated_users = [u for u in users if u["id"] != user_id]
#         self._write_data(updated_users)
#         return {"message": "User deleted successfully"}
#
#
# import json
# import os
#
# class UserService:
#     def __init__(self, file_path="app/data/users.json"):
#         self.file_path = file_path
#
#     def _read_data(self):
#         # If file doesn't exist, create it with an empty list
#         if not os.path.exists(self.file_path):
#             with open(self.file_path, "w") as f:
#                 json.dump([], f)
#
#         # Read data safely
#         with open(self.file_path, "r") as f:
#             try:
#                 return json.load(f)
#             except json.JSONDecodeError:
#                 return []  # Return empty list if file is empty or corrupted
#
#     def _write_data(self, data):
#         with open(self.file_path, "w") as f:
#             json.dump(data, f, indent=2)
class UserService:
    def __init__(self):
        self.file_path = "app/data/users.json"

    def _read_data(self):
        import json, os
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as file:
            return json.load(file)

    def _write_data(self, data):
        import json
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def create_user(self, user):
        users = self._read_data()
        new_user = {"id": len(users) + 1, "name": user.name, "email": user.email}
        users.append(new_user)
        self._write_data(users)
        return new_user

    def get_user(self, user_id: int):
        users = self._read_data()
        for user in users:
            if user["id"] == user_id:
                return user
        return {"error": "User not found"}

    def get_users(self):
        return self._read_data()

    def update_user(self, user_id: int, user_data):
        """✅ Update an existing user by ID"""
        users = self._read_data()
        for u in users:
            if u["id"] == user_id:
                u["name"] = user_data.name
                u["email"] = user_data.email
                self._write_data(users)
                return {"message": "User updated successfully", "user": u}
        return {"error": "User not found"}

    def delete_user(self, user_id: int):
        users = self._read_data()
        for i, user in enumerate(users):
            if user["id"] == user_id:
                deleted_user = users.pop(i)
                self._write_data(users)
                return {"message": "User deleted successfully", "user": deleted_user}
        return {"error": "User not found"}
