import { NextRequest, NextResponse } from 'next/server';
const mysql = require('mysql');

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password",
    database: "draft"
});

// Function to execute a MySQL query and return a promise
function executeQuery(query) {
    return new Promise((resolve, reject) => {
        db.query(query, (error, results) => {
            if (error) {
                reject(error);
            } else {
                resolve(results);
            }
        });
    });
}

export async function GET(
    request: NextRequest,
    response: NextResponse,
) {
    try {
        // Connect to the MySQL database
        await new Promise((resolve, reject) => {
            db.connect((err) => {
                if (err) {
                    console.error("Error connecting to the database:", err);
                    reject(err);
                } else {
                    console.log("Connected to MySQL server!");
                    resolve();
                }
            });
        });

        // Execute the query using the custom executeQuery function
        const query = "SELECT * FROM users";
        const customers = await executeQuery(query);

        console.log("Query result:", customers);

        db.end(); // Close the connection after the query is executed successfully.

        // Send the JSON response using the json helper from NextResponse
        return new NextResponse(JSON.stringify(customers), {
            headers: {
                'Content-Type': 'application/json',
            },
        });
    } catch (error) {
        console.error("Error executing the query:", error);
        // Send an error JSON response
        return new NextResponse(JSON.stringify({ error: "Failed to execute the query" }), {
            status: 500,
            headers: {
                'Content-Type': 'application/json',
            },
        });
    }
}
