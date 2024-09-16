import './App.css';

function App() {
  return (
      <table style={{width:'100%'}}>
          <tr style={{fontStyle:'italic', fontWeight:'bold', fontSize:'40px', backgroundColor:'grey'}}>
              <th>Welcome To My Store </th>
          </tr>
          <tr style={{height: "40px"}}></tr>
          <tr>
              <th>
                  <form>
                      <input type="text" placeholder={"Enter Your Name "}></input><br></br><br></br>
                      <input type="text" placeholder={"Enter Your father name "}></input><br></br><br></br>
                      <input type="text" placeholder={"Enter Your phone number "}></input><br></br><br></br>
                      <input type="email" placeholder={"Enter Your email address "}></input><br></br><br></br>
                      <input type="password" placeholder={"Enter Your Password"}></input><br></br><br></br>
                      <input type="submit" value="Login"></input><br></br>
                  </form>
              </th>
          </tr>
          </table>
);
}
export default App;
