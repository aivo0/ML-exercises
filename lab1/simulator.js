const calculatePercepts = state => ({
  room: state.agentPosition,
  roomState: state[state.agentPosition]
});

// Verbose enables console logging at every simulation step
function vacWorldSim(
  iniState = {},
  steps = 10,
  statefulAgent,
  agent,
  randomness,
  verbose = false
) {
  let percepts = {};
  let totalCost = 0;
  costTable = {
    Suck: 2,
    Left: 1,
    Right: 1,
    NoOp: 0,
    Dirty: 3,
    Clean: 0
  };
  const worldState = Object.assign({}, iniState);
  let agentState = {
    A: "Unknown",
    B: "Unknown"
  };
  let agentInput = [];
  if (verbose)
    console.log(
      `Starting state: room A is ${worldState.A}, room B is ${
        worldState.B
      } and agent is at room ${worldState.agentPosition}`
    );
  let randomInt = 0;
  for (i = 0; i < steps; i++) {
    if (randomness) {
      randomInt = Math.floor(Math.random() * 10);
      if (randomInt === 8) worldState.A = "Dirty";
      else if (randomInt === 9) worldState.B = "Dirty";
    }
    percepts = calculatePercepts(worldState);
    if (verbose) {
      console.log(`Step ${i + 1}:`);
      console.log(
        `Agent senses that room ${percepts.room} is ${percepts.roomState}`
      );
    }
    agentInput = statefulAgent ? agent(percepts, agentState) : agent(percepts);
    totalCost +=
      costTable[agentInput[0]] +
      costTable[worldState.A] +
      costTable[worldState.B];
    if (verbose) console.log(`Agent's action: ${agentInput[0]}`);
    if (agentInput === "NoOp") {
    } else if (
      agentInput[0] === "Suck" &&
      worldState[worldState.agentPosition] === "Dirty"
    )
      worldState[worldState.agentPosition] = "Clean";
    else if (agentInput[0] === "Right" && worldState.agentPosition === "A")
      worldState.agentPosition = "B";
    else if (agentInput[0] === "Left" && worldState.agentPosition === "B")
      worldState.agentPosition = "A";

    if (verbose)
      console.log(
        `Result: room A is ${worldState.A}, room B is ${
          worldState.B
        } and agent is at room ${worldState.agentPosition}`
      );
  }
  console.log(`Agent's total cost: ${totalCost}`);
}

// Agent with no memory. Always goes to the other room when the current is clean.
const reflexAgent = percepts => {
  let action;
  if (percepts.roomState === "Dirty") {
    action = "Suck";
  } else if (percepts.room === "A") action = "Right";
  else if (percepts.room === "B") action = "Left";
  else action = "NoOp";
  return [action];
};

// Agent who remebers where he cleaned and never goes there again if it was cleaned. Cleans current room if dirty again.
const stateReflexAgent = (percepts, state) => {
  let action;
  if (percepts.roomState === "Dirty") {
    action = "Suck";
    state[percepts.room] = "Clean";
  } else if (percepts.room === "A" && state.B !== "Clean") action = "Right";
  else if (percepts.room === "B" && state.A !== "Clean") action = "Left";
  else action = "NoOp";
  return [action, state];
};

const initialState = {
  A: "Dirty",
  B: "Dirty",
  agentPosition: "A"
};

console.log("State reflex agent - deterministic world");
vacWorldSim(initialState, 10, true, stateReflexAgent, false, false);
console.log("Reflex agent - deterministic world");
vacWorldSim(initialState, 10, false, reflexAgent, false, false);
console.log("State reflex agent - random world");
vacWorldSim(initialState, 20, true, stateReflexAgent, true, false);
console.log("Reflex agent - random world");
vacWorldSim(initialState, 20, false, reflexAgent, true, false);
