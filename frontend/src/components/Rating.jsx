import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faStar } from "@fortawesome/free-solid-svg-icons";


const Rating = ({ rating,  advicesCount }) => {
  const stars = [];

  for (let i = 0; i < rating; i++) {
    stars.push(<FontAwesomeIcon icon={faStar} key={i} color={"gold"}/>);
  }

  return <div>{stars} ({advicesCount})</div>;
};

export default Rating;
