import { Button } from 'rsuite';
import './customButton.css';          // Import custom CSS
function Button() {
  return (
    <div>
        <Button className= "custom-button">
            Go!
        </Button>
        
    </div>
  );
};

export default Button