db.createUser(
    {
        user: "root",
        pwd: "root",
        roles: [
            {
                role: "readWrite",
                db: "trends"
            }
        ]
    }
);
db.createCollection('trends');