const mysql = require('mysql');

const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "password",
  database: "draft"
});

// Function to execute a MySQL query and return a promise
function executeQuery(query, values) {
  return new Promise((resolve, reject) => {
    db.query(query, values, (error, results) => {
      if (error) {
        reject(error);
      } else {
        resolve(results);
      }
    });
  });
}


async function MYSQLcreate(formData){
  "use server";
  const query = "INSERT INTO users (first_name, last_name) VALUES (?, ?)";
  const values = [formData.get('first_name'), formData.get('last_name')];

  try {
    const results = await executeQuery(query, values);
  } catch (error) {
    console.error("Error executing the query:", error);
  }
}

export default function MYSQLInsert(){
    return(
        <div>
            <form action={MYSQLcreate}>
                <h1 >First name:</h1>
                <input type="text" name="first_name"/>
                <h1 >Last name:</h1>
                <input type="text"  name="last_name"/>
                <br></br>
                <button type="submit" style={{fontSize:"1.5rem"}}> Submit</button>
                
            </form>
        </div>   
    )
}