import { Checkmark } from 'react-checkmark'

const IsExpertVerified = ({ verified }) => {
return verified === "yes" ? (
    <Checkmark color="blue" size={"medium"}/>
  ) : null;
};

export default IsExpertVerified;
