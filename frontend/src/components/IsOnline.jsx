import { CircleFill } from "react-bootstrap-icons";

const ExpertStatus = ({ online }) => {
  return online === "yes" ? (
    <CircleFill color="green" />
  ) : (
    <CircleFill color="red" />
  );
};

export default ExpertStatus;
