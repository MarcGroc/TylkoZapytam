import { useState } from 'react';
import Card from 'react-bootstrap/Card';
import CardButton from "./CardButton";
import expertimg from "../images/expertimg.jpg";
import Rating from "./Rating";
import ExpertStatus from "./IsOnline";
import IsVerified from "./IsVerified";

// create function that will zoom in once the entire card when onhover and zoom out when onmouseleave

function zoomIn(e) {
    e.target.style.transform = "scale(1.1)";
    e.target.style.transition = "all 0.3s";

}


const ExpertTile =() => {
    let  imageUrl = "./public/expert.png";
    const [expert, setExpert] = useState([
        {key: 1, id: 1, fullName: "Tom", title: " I'm expert in Computer Science", rating: 4.5, advicesCount: 12, online: "yes", verified: "yes", imageUrl: expertimg},
        {key:2, id: 2, fullName: "Jane", title: " I'm expert in Psychology", rating: 5, advicesCount: 23, online: "yes",  verified: "no", image: imageUrl},
        {key:3, id: 3, fullName: "John", title: " I'm expert in Biology", rating: 4, advicesCount: 7, online: "no",  verified: "yes", image: imageUrl},
        {key:4, id: 4, fullName: "Dan", title: " I'm expert in Chemistry", rating: 5, advicesCount: 41, online: "yes",  verified: "yes", image: imageUrl},
        {key:5, id: 5, fullName: "Marc", title: " I'm expert in Marketing", rating: 5, advicesCount: 3, online: "no",  verified: "no", image: imageUrl},
        {key:6, id: 6, fullName: "Monika", title: " I'm expert in Project Management", rating: 5, advicesCount: 124,  verified: "yes", online: "yes", image: imageUrl},
        {key:7, id: 7, fullName: "Nicolas", title: " I'm expert in SEO", rating: 3, advicesCount: 1, online: "yes",  verified: "no", image: imageUrl},
        {key:8, id: 8, fullName: "Smith", title: " I'm expert in Travel", rating: 5, advicesCount: 22, online: "no",  verified: "yes", image: imageUrl},
        ]
    );
    function openExpertPageOnClick(e) {
        e.preventDefault();
        window.open("http://localhost:3000/expertpage");
    }
    return (
        <main className="container">
            <div className="col-sm-offset-0">
                <div className="card-collection"   style={{display: "grid", gridTemplateColumns: "1fr 1fr 1fr 1fr"}}>
                    {expert.map((expert) => (
                        <Card className="card m-4" onClick={openExpertPageOnClick}  style={{ width: '20rem', cursor: "pointer"}}>
                          <Card.Img variant="top" src={expertimg} /> <IsVerified verified={expert.verified}/>
                          <Card.Body>
                            <Card.Title>{expert.fullName}  <ExpertStatus online={expert.online}/>
                                <Rating rating={expert.rating} advicesCount={expert.advicesCount}/> </Card.Title>
                            <Card.Text>
                                {expert.title}
                            </Card.Text>
                            <CardButton />
                          </Card.Body>
                        </Card>
                        ))}
                </div>
            </div>
        </main>
    );
}

export default ExpertTile;