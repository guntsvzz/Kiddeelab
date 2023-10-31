Queries - KiddeeLab

Asset
https://mui.com/material-ui/getting-started/usage/
https://tailwindcss.com/docs/aspect-ratio
https://m3.material.io

MongDB with verbal
https://www.mongodb.com/developer/products/atlas/how-to-connect-mongodb-atlas-to-vercel-using-the-new-integration/

https://www.mongodb.com/developer/languages/javascript/nextjs-with-mongodb/

MySQL
https://dev.mysql.com/downloads/
MySQL Community Server
MySQL Workbench

Setting Password

Create Database 
2 Ways of creating table
https://drive.google.com/drive/u/2/folders/1xVV4ds_VT-mJ-dYjM23UG2U5Peqsmdg2
Laboratory2022 - Google Drive

https://drive.google.com/drive/u/2/folders/1UIKyvOGJKTVl-dlImnIWDsbGn0HwX4pe
Lab3_DMM - Google Drive

Changing password 
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
flush privileges;

1. Day-1 : Introduction of SQL
    1. Installing & Creating Table 0.5 hr
        1. Manual creating Table 0.5 hr
            1. Create scheme 
        2. Coding creating Table 1 hr
            1. Create 
            2. Read
            3. Update
            4. Delete (Skip)
    2. Basic Query 1.5 Hour
        1. Basic
        2. Aggregation
2. Day-2 : Diagram and Data
    1. Schema Diagram 
        1. ER Digram 2 Hours
        2. Mock Up Data 2 Hours
            1. SQL Server. Free Database. Free Download - Dofactory
3. Day-3 : Complex Query 4 Hours
        1. Joining Query
        2. Subqueries
4. Day-4 : Vercel with SQL

Resource
https://github.com/plkpiotr/soccer-league
https://www.sqltutorial.org/sql-sample-database/
databasestar/sample_databases at main · bbrumm/databasestar · GitHub
https://www.guru99.com/er-diagram-tutorial-dbms.html
Entity Relationship (ER) Diagram Model with DBMS Example (guru99.com)
https://www.sqlservertutorial.net
Day-4 Vercel + Postgress
https://vercel.com/docs/storage/vercel-postgres/quickstart
- Updating and install Vercel
npm i -g vercel@latest
npm i @vercel/postgres

- When u don’t want to use GitHub
npx create-next-app
vercel link
vercel env pull .env.development.local

- Appendix
App router no-> pages
Pages creating a file directly
App have to create folder/page.tsx

https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-serial/
Using PostgreSQL SERIAL To Create The Auto-increment Column (postgresqltutorial.com)



Day-3
https://www.w3schools.com/sql/sql_operators.asp
SQL Operators (w3schools.com)
https://www.dofactory.com/sql/subquery
SQL Subquery | Nested query - Dofactory
https://www.sqltutorial.org/sql-sample-database/
SQL Sample Database (sqltutorial.org)


Day4
- Create Vercel without connecting GitHub
- Postgres Vercel and constraint configurations
- Create Table via Postgres Verfcel
- Insert Table Via Postgres Vercel
- Creating table via .tsx file (Retreive SELECT * FROM)
- (Tentative) update 
- 

DROP TABLE fake;

CREATE TYPE gender_enum AS ENUM ('Male', 'Female', 'Non-binary');

CREATE TABLE IF NOT EXISTS fake ( 
        student_id SERIAL PRIMARY KEY, 
        first_name VARCHAR(255) NULL, 
        last_name VARCHAR(255) NULL,
        nickname VARCHAR(50) NULL,
        birthdate TIMESTAMP NULL,
        gender gender_enum NULL,
        school VARCHAR(100)
        );


sudo apt update && sudo apt upgrade
sudo apt install curl
curl --version
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
pip3 install --upgrade pip 
pip3 install pytokenizations

https://www.youtube.com/watch?v=bolW97Mrcc4
(28) Make Stunning AI Animations with Stable Diffusion Deforum Notebook in Google Colab - YouTube
https://weirdwonderfulai.art/resources/free-google-colab-notebooks-for-stable-diffusion/
Free Google Colab Notebooks for Stable Diffusion | Weird Wonderful AI Art
https://colab.research.google.com/github/deforum/stable-diffusion/blob/main/Deforum_Stable_Diffusion.ipynb
Deforum_Stable_Diffusion.ipynb - Colaboratory (google.com)



https://github.com/kipgparker/soft-prompt-tuning
kipgparker/soft-prompt-tuning (github.com)

1. Load dataset from Llm extraction google
2. Load prompt
Prefix as X and suffix as y
3. From accelerator import broadcast
4. Attacker 
    1. https://github.com/amazon-science/controlling-llm-memorization/blob/main/src/promptLearn_attack.py
    2. controlling-llm-memorization/src/promptLearn_attack.py at main · amazon-science/controlling-llm-memorization (github.com)
5. Defender 
    1. https://github.com/amazon-science/controlling-llm-memorization/blob/main/src/promptLearn_defense.py
    2. controlling-llm-memorization/src/promptLearn_defense.py at main · amazon-science/controlling-llm-memorization (github.com)
