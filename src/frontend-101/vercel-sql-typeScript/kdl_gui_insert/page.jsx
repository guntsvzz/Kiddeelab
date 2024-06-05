import {sql} from "@vercel/postgres";
import Image from 'next/image'

async function create(formData){
    "use server";
    const {rows} = await sql`INSERT INTO kdl_students
    VALUES(DEFAULT, ${formData.get('first_name')}, ${formData.get('last_name')}, ${formData.get('nickname')}, ${formData.get('birthdate')}, ${formData.get('gender')}, ${formData.get('school')})`;
}

export default function Insert(){
    return(
        <div>
            <form action={create}>
                <Image src='/next.svg' height={500} width={500} alt='next'></Image>
                <h1 >First name:</h1>
                <input type="text" name="first_name"/>
                <h1 >Last name:</h1>
                <input type="text"  name="last_name"/>
                <h1 >Nickname:</h1>
                <input type="text" name="nickname"/>
                <h1 >Birthdate name:</h1>
                <input type="text"  name="birthdate"/>
                <h1 >Gender:</h1>
                <input type="text" name="gender"/>
                <h1 >School:</h1>
                <input type="text"  name="school"/>
                <br></br>
                <button type="submit" style={{fontSize:"1.5rem"}}> Submit</button>
                
            </form>
        </div>   
    )
}