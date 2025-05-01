## Introduction
- This diagram represents the data preprocessing and query flow in a 5G system. It shows how raw logs and packet captures (PCAP) from various network components are transformed into structured, useful messages that can be queried for diagnostics, debugging, or automation.

![image](https://github.com/user-attachments/assets/bdc9d5db-d0c7-4ad8-afc9-b9024f0ce080)

## Input Data Sources
- gNB log
  - Logs from the gNB (Base station), such as RRC procedures, attach failures, or initialization errors.
- FH PCAP
  - Packet capture files from the FrontHaul interface (e.g., O-RAN C-Plane and U-Plane traffic).
- RU log
  - Logs from the Radio Unit, containing timing, RF state, and synchronization information.
- NGAP/NAS PCAP
  - Packet captures containing NGAP (Next Generation Application Protocol) and NAS (Non-Access Stratum) messages exchanged between the gNB and 5GC.

![image](https://github.com/user-attachments/assets/b1ca7768-7efc-4d99-9dd1-25ee4b57b893)

## Preprocessing Tools
- These tools extract specific, meaningful events or errors from raw inputs.
- Includes:
  - Keyword or pattern matching
  - Packet dissection using tools like tshark
  - Log parsing and structuring
- Outputs are concise, context-aware messages for each source.

![image](https://github.com/user-attachments/assets/21d12bdb-fb1d-41f7-a0b3-173434bf44dd)

## Component-Specific Useful Messages
- gNB Specific Useful Message
  - E.g., "RRC Setup timeout", "UE attach failed", "Invalid ciphering algorithm"
- FH Specific Useful Message
  - E.g., "Missing section packet", "Frame/slot mismatch", "Jump in counter"
- RU Specific Useful Message
  - E.g., "IQ width misconfigured", "RF not started", "Timing misalignment"
- NGAP/NAS Specific Useful Message
  - E.g., "InitialUEMessage received", "Authentication Failure", "PDU Session Setup Response delay"

![image](https://github.com/user-attachments/assets/1e60040b-8446-4120-b566-be33a3169bf8)


## Input – Debug Knowledge
- Debug yaml: A structured file that documents known symptoms, their causes, log snippets, and the related config fields.
- This is embedded into the Integration_Dataset, which serves as the retrieval base.

## Retrieval Stage
- Query (from the user or system): Describes an issue or request (e.g., “UE cannot attach”).
- The system uses similarity search over the Integration_Dataset to retrieve:
  - Symptom: Matched issue from the dataset.
  - Related config: Fields or parameters related to the symptom.

## Prompt Construction
Inputs to the prompt:
- Symptom and Related config (from retrieval)
- Query (from the user or diagnostic system)
- Reference_Config: A known-correct config (e.g., golden config or MAC/IP mapping)
- Current_Config: The configuration being debugged

All these are combined into a structured prompt, sent to the LLM.

## LLM Processing
- The LLM receives the full context and returns:
  - Suggestion: Specific config changes (e.g., integrity_algorithms = ( "nia2", "nia0" );)
  - Reason: Explanation for the recommendation (e.g., "matches supported algorithm pool, avoids negotiation failure")

## Final Output
Suggestions are applied to generate a New conf (new configuration file), ready for testing or deployment.





![image](https://github.com/user-attachments/assets/22d83209-a6a7-4d7f-a69f-53f5f43ca165)
