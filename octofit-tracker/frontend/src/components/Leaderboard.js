import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Leaderboard = () => {
  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Leaderboard</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Rank</th>
              <th>Name</th>
              <th>Points</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td>John Doe</td>
              <td>1500</td>
            </tr>
            <tr>
              <td>2</td>
              <td>Jane Smith</td>
              <td>1400</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Leaderboard;
