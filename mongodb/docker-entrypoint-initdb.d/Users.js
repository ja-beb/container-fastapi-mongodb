
db.createCollection("users");
db.users.createIndex({"email": 1}, {unique:true});
db.users.insertMany([
    {"name":"test user", "email": "test.user@test-site.org"},
    {"name":"test user 1", "email": "test.user1@test-site.org"},
    {"name":"test user 2", "email": "test.user2@test-site.org"},
    {"name":"test user 3", "email": "test.user3@test-site.org"}
]);
