import Image from 'next/image'
// import styles from './page.module.css'

import {db} from '@vercel/postgres'
import{NextApiResponse} from 'next'


export default async function Home() {
  
  async function getData(){

    const client = await db.connect()

    const customers = client.sql`SELECT * FROM kdl_students;`
    
    return customers
  }

  const data = await getData()

  let tableRows = data.rows
  console.log(tableRows)
  let keysArray = Object.keys(tableRows[0])
  console.log(keysArray)

  return (
    <main>
      <table>
        <tbody>
          <tr>
            {/* <th>student_id</th>
            <th>first_name</th>
            <th>last_name</th>
            <th>nickname</th>
            <th>birthdate</th>
            <th>gender</th>
            <th>school</th> */}
            {
            keysArray.map((key, index) => (
              <th key={index}>{key}</th>))
            }
          </tr>
            {
              tableRows.map((val,key)=> <tr key={key}>
                <td>{val.student_id}</td>
                <td>{val.first_name}</td>
                <td>{val.last_name}</td>
                <td>{val.nickname}</td>
                <td>{val.birthdate.toString()}</td>
                <td>{val.gender}</td>
                <td>{val.school}</td>
              </tr>)
            }
        </tbody>
      </table>
    </main>
  )
}