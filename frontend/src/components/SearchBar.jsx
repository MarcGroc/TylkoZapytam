import { Form, FormControl } from "react-bootstrap";

const MySearchBar = () => {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center" }}>
      <Form>
        <Form.Control
          type="text" size="lg"
          placeholder="Search for Name, Category, or Keyword"
          style={{ width: "700px", borderRadius: "25px" }}
        />
      </Form>
    </div>
  );
};

export default MySearchBar;
