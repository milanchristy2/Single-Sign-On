export const BASE_URL="http://localhost:8000/v1/github";
export async function login(){
   window.location.href=`${BASE_URL}/login`;
}
// export async function logout(){
//     await fetch(`${BASE_URL}/logout`,{
//         method:'POST',
//         credentials:"include",
//     });
// }
// export async function whoAmI(){
//     const res=await fetch(`${BASE_URL}/who`,{
//         credentials:"include"
//     });
//     return res.json();
// }
