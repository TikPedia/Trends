db = db.getSiblingDB('trends');

db.createUser(
    {
        user: "trending",
        pwd: "trending",
        roles: [
            {
                role: "readWrite",
                db: "trends"
            }
        ]
    }
);
db.createCollection('trends');