import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';

const CardButton = () => {
  return (
    <ButtonGroup aria-label="Basic example">
      <Button variant="primary">Quick question</Button>
      <Button variant="danger">Schedule Call</Button>
    </ButtonGroup>
  );
}

export default CardButton;