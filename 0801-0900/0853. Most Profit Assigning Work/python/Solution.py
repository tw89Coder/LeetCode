from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Main Idea:
        Sort cars by starting position in descending order (closest to target first). 
        A car fleet is formed when a car behind catches up to the car/fleet in 
        front. Since cars cannot pass each other, we only need to track the 
        arrival time of the 'slowest' lead car in front. If a trailing car 
        takes more time to arrive than the current lead car, it initiates 
        a new car fleet.

        Complexity:
            Time: O(n log n)
            Space: O(n)
        """
        # Step 1: Combine position and speed, then sort by position descending.
        # This allows us to process cars from the one closest to the target backwards.
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        # Tracks the arrival time of the slowest car (bottleneck) in the current fleet.
        last_fleet_time = -1.0
        
        for p, s in cars:
            # Step 2: Calculate the time required to reach the target.
            arrival_time = (target - p) / s
            
            # Step 3: Compare with the fleet in front.
            # If the current car takes STRICTLY more time than the fleet in front,
            # it cannot catch up. Therefore, it becomes the lead car of a new fleet.
            if arrival_time > last_fleet_time:
                fleets += 1
                # Update the bottleneck time to this car's arrival time.
                last_fleet_time = arrival_time
                
            # If arrival_time <= last_fleet_time, this car catches up and 
            # becomes part of the existing fleet, moving at the lead car's speed.
                
        return fleets

# --- Standalone Test Execution ---
if __name__ == "__main__":
    sol = Solution()
    # Case: Multiple cars forming different fleets
    print(f"Fleets: {sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])}") # Expected: 3