# Dream11 IPL Team Analyzer 🏏

A sophisticated application that helps users create optimal Dream11 teams for IPL cricket matches using advanced data analysis and machine learning concepts.

## 🌟 Features

- **Real-time Match Analysis**
  - Live match updates
  - Pitch condition analysis
  - Head-to-head statistics
  - Team win percentages

- **Smart Team Builder**
  - Advanced player selection algorithm
  - Role-based team composition
  - Credit optimization
  - Captain/Vice-captain recommendations

- **Performance Analytics**
  - Player form tracking
  - Venue-specific performance metrics
  - Opposition-based analysis
  - Historical performance data

- **Team Management**
  - Multiple team comparison
  - Draft team saving
  - Team validation
  - Performance predictions

## 💻 Tech Stack

- **Frontend**
  - React 19
  - TypeScript
  - Material-UI v7
  - Redux Toolkit
  - Recharts for data visualization
  - Vite for build tooling

- **State Management**
  - Redux for global state
  - Local storage for team persistence
  - Real-time updates

## 🏗️ Project Structure

```
ipl-dream11-analyzer/
├── src/
│   ├── api/          # API configurations and endpoints
│   ├── components/   # React components
│   ├── features/     # Redux slices and features
│   ├── services/     # Business logic and data services
│   ├── store/        # Redux store configuration
│   ├── types/        # TypeScript type definitions
│   └── utils/        # Utility functions and helpers
├── public/           # Static assets
└── tests/           # Test suites
```

## 🚀 Getting Started

### Prerequisites

- Node.js (v18 or higher)
- npm (v9 or higher)

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd ipl-dream11-analyzer
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Build for production:
```bash
npm run build
```

## 📋 Team Building Rules

The application enforces the following Dream11 team composition rules:

- Total Players: 11
- Maximum players from one team: 7
- Credit limit: 100
- Role requirements:
  - Wicket Keeper: 1
  - Batsmen: 3-5
  - All-rounders: 1-3
  - Bowlers: 3-5

## 🔍 Analysis Features

### Pitch Analysis
- Historical venue statistics
- Batting/Bowling conditions
- Chase success rates
- Weather impact

### Player Form Analysis
- Recent performance metrics
- Venue-specific records
- Opposition records
- Role effectiveness

### Team Comparison
- Statistical analysis
- Strength/weakness evaluation
- Performance predictions
- Historical head-to-head

## 🛠️ Development Commands

```bash
# Start development server
npm run dev

# Build production version
npm run build

# Run linting
npm run lint

# Preview production build
npm run preview
```

## 📈 Performance Metrics

The application calculates player performance using various metrics:

```typescript
interface PlayerMetrics {
    recentForm: number;        // 0-1 scale
    venuePerformance: number;  // 0-1 scale
    oppositionRecord: number;  // 0-1 scale
    roleValue: number;         // Role-based importance
}
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details

## 💡 Acknowledgments

- Dream11 for inspiration
- IPL for cricket data
- Cricket statisticians and analysts
- Open source community

## 🔮 Future Enhancements

- Machine learning-based team predictions
- Player price prediction
- Integration with live match data
- Mobile application
- Social features for team sharing
- Tournament-wise analytics
