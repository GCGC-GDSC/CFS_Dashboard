import React from 'react'
import {firebase} from "../../backend/firebase.config"
import {ReactComponent as Login} from "../../assets/login.svg"
import './Signin.styles.scss';

import gicon from "../../assets/GIcon.png"

function Signin() {
    const SiginiWithFirebase =() =>{
        const google_provider = new firebase.auth.GoogleAuthProvider()
        firebase.auth().signInWithPopup(google_provider)
        .then(user=>{
            // console.log(user)
        })
        .catch(err=>{
            console.log(err)
        })
    }
    return (

        <div className='sign-in'>
        <Login/>
        <button type="button"  className="login-with-google-btn" onClick = {SiginiWithFirebase}>
            <table>
                <tr>
                    <td className='GIconTD'><img className="GIcon" src={gicon} alt="google G" /></td>
                    <td>
                    
                        Sign in with Google
                    
                    </td>
                </tr>
            </table>
        </button>
        
       
    </div>  
 
    )
}
export default Signin