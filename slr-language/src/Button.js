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
        <div className="custom-button" style={{ display: 'flex', justifyContent: 'center'}} onClick={handleButtonClick}>
            <Button>
              Open Camera // label for camera button
            </Button>
        </div>
    </div>
  );
}

export default CustomButton;
