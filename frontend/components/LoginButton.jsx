"use client";
export default function LoginButton(){
    const login=()=>{
        window.location.href="http://localhost:8000/v1/github/login"
    };
    return(
        <button onClick={login} className="px-6 py-3 bg-black text-white rounded-lg">
            Login with Github
        </button>
    );
}