from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()

# 1. UserProfile model to store user information
class UserProfile(Base):
    __tablename__ = 'user_profiles'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    
    # Relationship to GameSession
    game_sessions = relationship('GameSession', back_populates='user')

# 2. GameSession model to track each session of gaming
class GameSession(Base):
    __tablename__ = 'game_sessions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_profiles.id'), nullable=False)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    games_played = Column(Integer, default=0)  # Number of games played in this session
    
    # Relationship to UserProfile
    user = relationship('UserProfile', back_populates='game_sessions')
    
    # Relationship to GameHistory
    game_histories = relationship('GameHistory', back_populates='session')

# 3. GameHistory model to track the outcome of each game played
class GameHistory(Base):
    __tablename__ = 'game_histories'
    
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('game_sessions.id'), nullable=False)
    game_name = Column(String(50), nullable=False)
    outcome = Column(String(10))  # e.g., Win, Lose, Draw
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    # Relationship to GameSession
    session = relationship('GameSession', back_populates='game_histories')

# 4. Leaderboard model to track top scores
class Leaderboard(Base):
    __tablename__ = 'leaderboard'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    game_name = Column(String(50), nullable=False)
    score = Column(Integer, default=0)  # Top scores for specific games



# Create the SQLite engine
engine = create_engine('sqlite:///escapepad.db')
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
