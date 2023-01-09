import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

// create function to show which experts are online and redirect to new page with filed results


const Navigation = () => {
  return (
    <>
      <Navbar variant="dark" style={{paddingBottom:"1rem",  background:"lightblue"}}>
        <Container>
          <Navbar.Brand href="#home" style={{ color: "black", fontSize: "30px" }}>Ask expert!</Navbar.Brand>
          <Nav className="justify-content-center" >
            <Nav.Link href="/whosonline"  style={{ color: "black", fontSize: "20px" }}>Who's Online </Nav.Link>
            <Nav.Link href="/category" style={{ color: "black", fontSize: "20px" }}>Category</Nav.Link>
          </Nav>
          <Nav className="justify-content-end" style={{ color: "black", fontSize: "20px" }}>
              <Nav.Link href="/account" style={{ color: "black", fontSize: "20px" }}>Account</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
        <div className={"bg-info"}>
            <h3 style={{ display: "flex", alignItems: "center", justifyContent: "center", paddingBottom: "20px", paddingTop: "20px" }}>Contact with experts or mentors and pay per minute!</h3>
        </div>
      <br />
    </>
  );
}

export default Navigation;