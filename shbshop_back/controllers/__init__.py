from . import home, auth, start, admin, test

blueprints = [
    (home.home_bp, "/home"),
    (auth.auth_bp, "/auth"),
    (start.start_bp, "/start"),
    (admin.admin_bp, "/admin"),
    (test.test_bp, "/test")
]