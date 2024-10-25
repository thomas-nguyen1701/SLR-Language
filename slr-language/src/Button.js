// Button.js
import { useNavigate } from 'react-router-dom';
import { Button } from 'rsuite'; // Import rsuite Button
import './customButton.css';     // Import custom CSS for styling

function CustomButton() {
  const navigate = useNavigate();

  const handleButtonClick = () => {
    navigate('/camera');
  };

  return (
    <div>
        <Button className="custom-button" onClick={handleButtonClick}>
            Open Camera
        </Button>
    </div>
  );
}

export default CustomButton;
