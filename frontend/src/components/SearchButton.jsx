import { Button } from "react-bootstrap";

const SearchButton = () => {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center", paddingBottom: "1rem", paddingTop: "1rem"}}>
      <Button variant="primary" size="lg" style={{width:"700px", borderRadius: "25px"}}>Search for Expert</Button>
    </div>
  );
};

export default SearchButton;
