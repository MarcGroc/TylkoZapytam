import React, { useState } from "react";
import Button from 'react-bootstrap/Button';


const Login = (props) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    props.onSubmit(email, password);
  };

  return (
        <Button  variant="primary" type="submit" style={{
        position: "absolute",
        top: "50px",
        right: "50px",
        }}> Login </Button>
  );
}

export default Login;
