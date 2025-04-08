import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Teams = () => {
  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Teams</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Team Name</th>
              <th>Members</th>
              <th>Points</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Team Alpha</td>
              <td>5</td>
              <td>1200</td>
            </tr>
            <tr>
              <td>Team Beta</td>
              <td>4</td>
              <td>1100</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Teams;
