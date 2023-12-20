from typing import List
#Made by Isbah, Jamin, Mikail

def compute(List, node) :
   #Metrics To Calculate
   i = 0
   String =  ' '
   SentReq = 0
   RecRep = 0
   RecReq = 0
   SentRep = 0
   TotalReqSent = 0
   source = 0
   RequestNo = 0
   count = 0
   corresponding = 1 #value to check for corresponding Echo Request and Reply
   rtt = 0
   TimeNano = 0
   counter=0
   goodput = 0
   delay = 0
   TotalReqRec = 0
   DataReqSent = 0
   DataReqRec = 0
   RequestTime = 0
   ReplyNo = 0
   ReplyTime = 0
   sumTTL = 0

   #Sets source ip to each Node
   if node == 1:
      source = "192.168.100.1"
   if node == 2:
      source = "192.168.100.2"
   if node == 3:
      source = "192.168.200.1"
   if node == 4:
      source = "192.168.200.2"
   reply = "reply"
   request = "request" 
   destination = "destination"
   #For Loop To Iterate Through Info List 
   for x in List:
      #Calculate The Amount of Requests Sent
      if List[i][2] == source and List[i][8] == request:
         SentReq = SentReq + 1 
         #Total Echo Requests Bytes Sent
         TotalReqSent =  TotalReqSent + int(List[i][5]) 

         DataReqSent =  DataReqSent + (int(List[i][5])-42)
         RequestNo = List[i][0]
         RequestTime = List[i][1]
         goodput += (float(List[i][5])-42)/1000
         

      #Calculate The Amount of Requests Recieved
      if List[i][3] == source and List[i][8] == request:
         TotalReqRec =  TotalReqRec + int(List[i][5]) 
         DataReqRec =  DataReqRec + (int(List[i][5])-42)
         RecReq = RecReq + 1
         RequestNo = List[i][0]
         RequestTime = List[i][1]
         if(int(List[i+1][0]) - int(List[i][0]) == corresponding):
            delay += (float(List[i+1][1]) - float(List[i][1])) * 1000000
            counter += 1
      #Calculate The Amount of Replies sent
      if List[i][2] == source and List[i][8] == reply:
         SentRep = SentRep + 1 
         ReplyNo = List[i][0]
         ReplyTime = List[i][1]
         

      #Calculate The Amount of Replies Recieved
      if List[i][3] == source and List[i][8] == reply:
         RecRep = RecRep + 1 

         ReplyNo = List[i][0]
         ReplyTime = List[i][1]
         if (int(ReplyNo) - int(RequestNo)) == corresponding:
            TimeNano = TimeNano + (float(ReplyTime) - float(RequestTime))
            if List[i][6] != destination:
              TTL = List[i][11]
              #Combines each number from the TTL metric
              sTTL = TTL[4] + TTL[5] + TTL[6]
              #Hop count finder
              sumTTL = sumTTL + (129 - int(sTTL))
              #Sum of ea$
              count = count +1
              
      i= i + 1

   #Average Ping Round Trip Time (RTT)
   rtt = round(((TimeNano / float(128)) / 0.001), 2)

   #Echo Request Throughput
   throughput = round((float(TotalReqSent)/float(TimeNano) * 0.001), 1)
   
   
   #Echo Request Goodput
   avggoodput = round(goodput/TimeNano, 1)
   
   #Average Reply Delay
   avgrplydelay = round(delay/counter, 2)
   
   #Average HopCount
   avgHopCount = round(sumTTL/count,2)
   
   #All of the values calculated above will be returned
   return SentReq, RecReq, SentRep, RecRep, TotalReqSent, TotalReqRec, DataReqSent, DataReqRec, rtt, throughput, avggoodput, avgrplydelay, avgHopCount


#Compute Metrics: This function takes the list from packet_parser and calculates SentReq, RecReq, SentRep, RecRep, TotalReqSent,
#TotalReqRec, DataReqSent, DataReqRec, rtt, throughput, avggoodput, avgrplydelay, avgHopCount and returns it.
