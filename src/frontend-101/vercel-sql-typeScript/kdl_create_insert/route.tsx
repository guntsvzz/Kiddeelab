import { db } from '@vercel/postgres';
import { NextRequest, NextResponse } from 'next/server';
// http GET
// handler
export async function GET(
  request: NextRequest,
  response: NextResponse,
) {
    const client = await db.connect();
    // SERIAL = AUTO_INCREMENT

    // await client.sql`CREATE TYPE gender_enum AS ENUM ('Male', 'Female', 'Non-binary');`; //creating enumerate gender

    await client.sql`CREATE TABLE IF NOT EXISTS kdl_students ( 
        student_id SERIAL PRIMARY KEY, 
        first_name VARCHAR(255) NULL, 
        last_name VARCHAR(255) NULL,
        nickname VARCHAR(50) NULL,
        birthdate TIMESTAMP NULL,
        gender VARCHAR(10) NULL,
        school VARCHAR(100) NULL
        );`;

    const names = ['Todsavad', 'Tangtortan','Gun','1999-09-28','Male','AIT'];
    await client.sql`INSERT INTO kdl_students 
      VALUES (DEFAULT, ${names[0]}, ${names[1]}, ${names[2]}, ${names[3]}, ${names[4]}, ${names[5]});`;

    const stds = await client.sql`SELECT * FROM kdl_students;`;
    const results =  NextResponse.json({ stds : stds.rows });
    return results
}