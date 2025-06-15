import { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    'Player 1 Name': '',
    'Player 2 Name': '',
    'Player 1 Ranking': '',
    'Player 2 Ranking': '',
    'Player 1 Form': '',
    'Player 2 Form': '',
    'Head-to-Head Record': '',
  });
  
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      const dataToSend = {
        'Player 1 Ranking': parseInt(formData['Player 1 Ranking']),
        'Player 2 Ranking': parseInt(formData['Player 2 Ranking']),
        'Player 1 Form': parseFloat(formData['Player 1 Form']),
        'Player 2 Form': parseFloat(formData['Player 2 Form']),
        'Head-to-Head Record': formData['Head-to-Head Record'],
      };
      
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSend),
      });
      
      if (!response.ok) {
        throw new Error('Failed to get prediction');
      }
      
      const result = await response.json();
      
      setPrediction({
        ...result,
        player1Name: formData['Player 1 Name'] || 'Player 1',
        player2Name: formData['Player 2 Name'] || 'Player 2'
      });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Wimbledon Match Prediction</h1>
        
        <div className="prediction-form">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label>Player 1 Name:</label>
              <input 
                type="text" 
                name="Player 1 Name" 
                value={formData['Player 1 Name']} 
                onChange={handleChange}
                placeholder="e.g., Novak Djokovic"
              />
            </div>
            
            <div className="form-group">
              <label>Player 2 Name:</label>
              <input 
                type="text" 
                name="Player 2 Name" 
                value={formData['Player 2 Name']} 
                onChange={handleChange}
                placeholder="e.g., Rafael Nadal"
              />
            </div>
            
            <div className="form-group">
              <label>Player 1 Ranking:</label>
              <input 
                type="number" 
                name="Player 1 Ranking" 
                value={formData['Player 1 Ranking']} 
                onChange={handleChange}
                required 
                min="1"
              />
            </div>
            
            <div className="form-group">
              <label>Player 2 Ranking:</label>
              <input 
                type="number" 
                name="Player 2 Ranking" 
                value={formData['Player 2 Ranking']} 
                onChange={handleChange}
                required 
                min="1"
              />
            </div>
            
            <div className="form-group">
              <label>Player 1 Form (0-1):</label>
              <input 
                type="number" 
                name="Player 1 Form" 
                value={formData['Player 1 Form']} 
                onChange={handleChange}
                required 
                step="0.01" 
                min="0" 
                max="1"
              />
            </div>
            
            <div className="form-group">
              <label>Player 2 Form (0-1):</label>
              <input 
                type="number" 
                name="Player 2 Form" 
                value={formData['Player 2 Form']} 
                onChange={handleChange}
                required 
                step="0.01" 
                min="0" 
                max="1"
              />
            </div>
            
            <div className="form-group">
              <label>Head-to-Head Record (format: wins-losses):</label>
              <input 
                type="text" 
                name="Head-to-Head Record" 
                value={formData['Head-to-Head Record']} 
                onChange={handleChange}
                placeholder="e.g., 3-1" 
                pattern="\d+-\d+"
              />
            </div>
            
            <button type="submit" disabled={loading}>
              {loading ? 'Processing...' : 'Predict Winner'}
            </button>
          </form>
          
          {error && <p className="error">Error: {error}</p>}
          
          {prediction && (
            <div className="prediction-result">
              <h2>Prediction Result</h2>
              <p className="winner">
                <strong>
                  {prediction.prediction === 'Player 1 Wins' 
                    ? prediction.player1Name 
                    : prediction.player2Name}
                  {' will likely win!'}
                </strong>
              </p>
              <p className="matchup">
                {prediction.player1Name} vs {prediction.player2Name}
              </p>
            </div>
          )}
        </div>
      </header>
    </div>
  );
}

export default App;
