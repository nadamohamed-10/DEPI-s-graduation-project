Dataset contains information about traffic accidents including:
Weather Conditions (Weather_Condition, Temperature(F), Wind_Chill(F), Humidity(%), Pressure(in), Visibility(mi), Wind_Speed(mph), Wind_Direction, 
Precipitation(in), Sunrise_Sunset)

Road Infrastructure Features (Junction, Crossing, Give_Way, No_Exit, Railway, Traffic_Signal, Bump, Roundabout, Station, Stop, Traffic_Calming, 
Turning_Loop)

Accident Timetable (Temporal Data, Start_Time, End_Time, Severity, Distance(mi))

Location (Street, City, State, Country, Amenity)
----------------------------------------------------------------------------------------------------------------------------------------------------
Data Cleaning Steps:
Removed unnecessary columns
Convert Start_Time and End_Time into datetime 
Extracted new time-based features(Year, Month, Day, Hour)
Handled missing values:
Numerical: used median 
Categorical: used mode
Precipitation : filled with 0
Delete duplicates
Boxplots for detecting outliers:
(Distance(mi), Wind_Speed(mph), Visibility(mi), Humidity(%), Wind_Chill(F), Temperature(F), Precipitation(in), Pressure(in)) ->left it because it's real
-----------------------------------------------------------------------------------------------------------------------------------------------------
