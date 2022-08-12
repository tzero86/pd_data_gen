import datetime
import json
import random
import os
addresses_list = [ ## For data generator, the bestrandom.com page only allows up to 10 requests at a time (Use either 10 zipcodes, or 10 runs)
 
 {  "address": "1775 Liberty Ln #70", "city": "Blacksburg", "zip": "24060", "state": "VA" }, 

{  "address": "2004 Scott Dr", "city": "Blacksburg", "zip": "24060", "state": "VA" }, 

{  "address": "3245 Laurel Dr", "city": "Blacksburg", "zip": "24060", "state": "VA" }, 

{  "address": "415 Giles Rd", "city": "Blacksburg", "zip": "24060", "state": "VA" }, 

{  "address": "3610 S Main St", "city": "Blacksburg", "zip": "24060", "state": "VA" }, 

{  "address": "307 Ardmore St", "city": "Blacksburg", "zip": "24060", "state": "VA" }, 

{  "address": "210 Prices Fork Rd #6", "city": "Blacksburg", "zip": "24060", "state": "VA" },

{  "address": "5560 Norris Run Rd", "city": "Blacksburg", "zip": "24060", "state": "VA" }, 

{  "address": "3020 Lick Run Rd", "city": "Blacksburg", "zip": "24060", "state": "VA" }, 

{  "address": "2834 Peppers Ferry Rd", "city": "Christiansburg", "zip": "24073", "state": "VA" }, 

{  "address": "295 Lucas St NE", "city": "Christiansburg", "zip": "24073", "state": "VA" }, 

{  "address": "1785 Electric Way #APT 2", "city": "Christiansburg", "zip": "24073", "state": "VA" }, 

{  "address": "265 Tanglewood Dr", "city": "Christiansburg", "zip": "24073", "state": "VA" }, 

{  "address": "140 Windsong Ln", "city": "Christiansburg", "zip": "24073", "state": "VA" }, 

{  "address": "515 Falling Branch Rd", "city": "Christiansburg", "zip": "24073", "state": "VA" }, 

{  "address": "385 Cheverly Rd", "city": "Christiansburg", "zip": "24073", "state": "VA" }, 

{  "address": "1825 Cambria St NE", "city": "Christiansburg", "zip": "24073", "state": "VA" },

{  "address": "781 Talon Ln", "city": "Christiansburg", "zip": "24073", "state": "VA" }, 

{  "address": "28 Carriage House Cir", "city": "Alexandria", "zip": "22304", "state": "VA" }, 

{  "address": "28 Carriage House Cir", "city": "Alexandria", "zip": "22304", "state": "VA" }, 

{  "address": "5375 Duke St #APT 209", "city": "Alexandria", "zip": "22304", "state": "VA" }, 

{  "address": "5375 Duke St #APT 209", "city": "Alexandria", "zip": "22304", "state": "VA" }, 

{  "address": "36 S Gordon St", "city": "Alexandria", "zip": "22304", "state": "VA" },

{  "address": "36 S Gordon St", "city": "Alexandria", "zip": "22304", "state": "VA" }, 

{  "address": "145 Century Dr #5102", "city": "Alexandria", "zip": "22304", "state": "VA" }, 

{  "address": "145 Century Dr #5102", "city": "Alexandria", "zip": "22304", "state": "VA" }, 

{  "address": "519 N Ripley St", "city": "Alexandria", "zip": "22304", "state": "VA" }, 

{  "address": "2610 Foundry Way", "city": "Alexandria", "zip": "22314", "state": "VA" }, 

{  "address": "2610 Foundry Way", "city": "Alexandria", "zip": "22314", "state": "VA" }, 

{  "address": "611 N Patrick St", "city": "Alexandria", "zip": "22314", "state": "VA" }, 

{  "address": "611 N Patrick St", "city": "Alexandria", "zip": "22314", "state": "VA" }, 

{  "address": "823 Rivergate Pl", "city": "Alexandria", "zip": "22314", "state": "VA" },

{  "address": "823 Rivergate Pl", "city": "Alexandria", "zip": "22314", "state": "VA" }, 

{  "address": "507 S Columbus St", "city": "Alexandria", "zip": "22314", "state": "VA" }, 

{  "address": "507 S Columbus St", "city": "Alexandria", "zip": "22314", "state": "VA" }, 

{  "address": "996 N Royal St", "city": "Alexandria", "zip": "22314", "state": "VA" }, 

{  "address": "2000 N Adams St #423", "city": "Arlington", "zip": "22201", "state": "VA" }, 

{  "address": "2000 N Adams St #423", "city": "Arlington", "zip": "22201", "state": "VA" }, 

{  "address": "1040 N Quincy St #401", "city": "Arlington", "zip": "22201", "state": "VA" }, 

{  "address": "910 S Buchanan St", "city": "Arlington", "zip": "22204", "state": "VA" }, 

{  "address": "910 S Buchanan St", "city": "Arlington", "zip": "22204", "state": "VA" }, 

{  "address": "835 S Greenbrier St", "city": "Arlington", "zip": "22204", "state": "VA" }, 

{  "address": "835 S Greenbrier St", "city": "Arlington", "zip": "22204", "state": "VA" }, 

{  "address": "1077 S Quebec St", "city": "Arlington", "zip": "22204", "state": "VA" }, 

{  "address": "1077 S Quebec St", "city": "Arlington", "zip": "22204", "state": "VA" }, 

{  "address": "3724 5th St S", "city": "Arlington", "zip": "22204", "state": "VA" }, 

{  "address": "3724 5th St S", "city": "Arlington", "zip": "22204", "state": "VA" }, 

{  "address": "1414 S Queen St", "city": "Arlington", "zip": "22204", "state": "VA" }, 

{  "address": "2312 N Wakefield St", "city": "Arlington", "zip": "22207", "state": "VA" }, 

{  "address": "2312 N Wakefield St", "city": "Arlington", "zip": "22207", "state": "VA" }, 

{  "address": "4733 Rock Spring Rd", "city": "Arlington", "zip": "22207", "state": "VA" }, 

{  "address": "4733 Rock Spring Rd", "city": "Arlington", "zip": "22207", "state": "VA" }, 

{  "address": "4124 N Richmond St", "city": "Arlington", "zip": "22207", "state": "VA" }, 

{  "address": "4124 N Richmond St", "city": "Arlington", "zip": "22207", "state": "VA" }, 

{  "address": "4069 27th Rd N", "city": "Arlington", "zip": "22207", "state": "VA" }, 

{  "address": "4069 27th Rd N", "city": "Arlington", "zip": "22207", "state": "VA" }, 

{  "address": "3515 36th St N", "city": "Arlington", "zip": "22207", "state": "VA" },

{  "address": "1700 Sherwood Hall Ln", "city": "Alexandria", "zip": "22306", "state": "VA" }, 

{  "address": "1700 Sherwood Hall Ln", "city": "Alexandria", "zip": "22306", "state": "VA" }, 

{  "address": "1629 Courtland Rd", "city": "Alexandria", "zip": "22306", "state": "VA" }, 

{  "address": "1629 Courtland Rd", "city": "Alexandria", "zip": "22306", "state": "VA" }, 

{  "address": "2629 Arlington Dr #302", "city": "Alexandria", "zip": "22306", "state": "VA" }, 

{  "address": "2629 Arlington Dr #302", "city": "Alexandria", "zip": "22306", "state": "VA" },

{  "address": "2720 Boswell Ave", "city": "Alexandria", "zip": "22306", "state": "VA" }, 

{  "address": "2720 Boswell Ave", "city": "Alexandria", "zip": "22306", "state": "VA" }, 

{  "address": "3006 Furman Ln", "city": "Alexandria", "zip": "22306", "state": "VA" }, 

{  "address": "9395 Mount Vernon Cir", "city": "Alexandria", "zip": "22309", "state": "VA" }, 

{  "address": "9395 Mount Vernon Cir", "city": "Alexandria", "zip": "22309", "state": "VA" }, 

{  "address": "4333 Pembrook Village Dr", "city": "Alexandria", "zip": "22309", "state": "VA" }, 

{  "address": "4333 Pembrook Village Dr", "city": "Alexandria", "zip": "22309", "state": "VA" }, 

{  "address": "5117 Pole Rd", "city": "Alexandria", "zip": "22309", "state": "VA" },

{  "address": "5117 Pole Rd", "city": "Alexandria", "zip": "22309", "state": "VA" }, 

{  "address": "8014 Imperial St", "city": "Alexandria", "zip": "22309", "state": "VA" },

{  "address": "8014 Imperial St", "city": "Alexandria", "zip": "22309", "state": "VA" }, 

{  "address": "8407 Byers Dr", "city": "Alexandria", "zip": "22309", "state": "VA" }, 

{  "address": "4111 Ivanhoe Ln", "city": "Alexandria", "zip": "22310", "state": "VA" }, 

{  "address": "4111 Ivanhoe Ln", "city": "Alexandria", "zip": "22310", "state": "VA" }, 

{  "address": "6065 Essex House Sq #A", "city": "Alexandria", "zip": "22310", "state": "VA" }, 

{  "address": "6065 Essex House Sq #A", "city": "Alexandria", "zip": "22310", "state": "VA" }, 

{  "address": "6523 Riefton Ct", "city": "Alexandria", "zip": "22310", "state": "VA" },

{  "address": "6523 Riefton Ct", "city": "Alexandria", "zip": "22310", "state": "VA" }, 

{  "address": "6612 Glassell Ct", "city": "Alexandria", "zip": "22310", "state": "VA" }, 

{  "address": "6905 Victoria Dr #D", "city": "Alexandria", "zip": "22310", "state": "VA" },

{  "address": "5872 Woodfield Estates Dr", "city": "Alexandria", "zip": "22310", "state": "VA" }, 

{  "address": "6547 River Tweed Ln", "city": "Alexandria", "zip": "22312", "state": "VA" }, 

{  "address": "6547 River Tweed Ln", "city": "Alexandria", "zip": "22312", "state": "VA" }, 

{  "address": "6609 Jupiter Hills Cir", "city": "Alexandria", "zip": "22312", "state": "VA" }, 

{  "address": "6609 Jupiter Hills Cir", "city": "Alexandria", "zip": "22312", "state": "VA" }, 

{  "address": "5851 Quantrell Ave #APT 307", "city": "Alexandria", "zip": "22312", "state": "VA" }, 

{  "address": "5851 Quantrell Ave #APT 307", "city": "Alexandria", "zip": "22312", "state": "VA" },

{  "address": "6117 Berlee Dr", "city": "Alexandria", "zip": "22312", "state": "VA" }, 

{  "address": "6117 Berlee Dr", "city": "Alexandria", "zip": "22312", "state": "VA" }, 

{  "address": "5618 Bloomfield Dr #10", "city": "Alexandria", "zip": "22312", "state": "VA" },

{  "address": "8113 Saxony Dr", "city": "Annandale", "zip": "22003", "state": "VA" }, 

{  "address": "3326 Woodburn Village Dr #34", "city": "Annandale", "zip": "22003", "state": "VA" }, 

{  "address": "7200 Pine Dr", "city": "Annandale", "zip": "22003", "state": "VA" }, 

{  "address": "7401 Eastmoreland Rd #APT 202", "city": "Annandale", "zip": "22003", "state": "VA" }, 

{  "address": "7401 Eastmoreland Rd #APT 412", "city": "Annandale", "zip": "22003", "state": "VA" },

{  "address": "4416 Island Pl #102", "city": "Annandale", "zip": "22003", "state": "VA" }, 

{  "address": "4437 Elan Ct", "city": "Annandale", "zip": "22003", "state": "VA" }, 

{  "address": "6833 Pacific Ln", "city": "Annandale", "zip": "22003", "state": "VA" }, 

{  "address": "4135 Watkins Trl", "city": "Annandale", "zip": "22003", "state": "VA" }, 

{  "address": "5827 Cove Landing Rd #APT 301", "city": "Burke", "zip": "22015", "state": "VA" }, 

{  "address": "10715 Oakenshaw Ct", "city": "Burke", "zip": "22015", "state": "VA" }, 

{  "address": "5819 Pin Oak Commons Ct", "city": "Burke", "zip": "22015", "state": "VA" }, 

{  "address": "5906 Bridgetown Ct #37", "city": "Burke", "zip": "22015", "state": "VA" }, 

{  "address": "9605 Woodedge Dr", "city": "Burke", "zip": "22015", "state": "VA" }, 

{  "address": "10203 Chase Commons Dr", "city": "Burke", "zip": "22015", "state": "VA" },

{  "address": "6330 Falling Brook Dr", "city": "Burke", "zip": "22015", "state": "VA" }, 

{  "address": "5837 Cove Landing Rd #301", "city": "Burke", "zip": "22015", "state": "VA" }, 

{  "address": "10095 Bunker Woods Ct", "city": "Burke", "zip": "22015", "state": "VA" }, 

{  "address": "5114 Castle Way Hbr", "city": "Centreville", "zip": "20120", "state": "VA" }, 

{  "address": "5114 Castle Way Hbr", "city": "Centreville", "zip": "20120", "state": "VA" }, 

{  "address": "6200 Point Cir", "city": "Centreville", "zip": "20120", "state": "VA" }, 

{  "address": "6200 Point Cir", "city": "Centreville", "zip": "20120", "state": "VA" }, 

{  "address": "6553 Hallissey Ct", "city": "Centreville", "zip": "20120", "state": "VA" }, 

{  "address": "6553 Hallissey Ct", "city": "Centreville", "zip": "20120", "state": "VA" }, 

{  "address": "15009 Carlbern Dr", "city": "Centreville", "zip": "20120", "state": "VA" }, 

{  "address": "15009 Carlbern Dr", "city": "Centreville", "zip": "20120", "state": "VA" },

{  "address": "5636 Willoughby Newton Dr #16", "city": "Centreville", "zip": "20120", "state": "VA" },
{  "address": "6211 Centreville Rd #800", "city": "Centreville", "zip": "20121", "state": "VA" }, 

{  "address": "6211 Centreville Rd #800", "city": "Centreville", "zip": "20121", "state": "VA" }, 

{  "address": "14816 Edman Cir", "city": "Centreville", "zip": "20121", "state": "VA" }, 

{  "address": "14816 Edman Cir", "city": "Centreville", "zip": "20121", "state": "VA" }, 

{  "address": "14309 Climbing Rose Way #203", "city": "Centreville", "zip": "20121", "state": "VA" }, 

{  "address": "14309 Climbing Rose Way #203", "city": "Centreville", "zip": "20121", "state": "VA" }, 

{  "address": "6455 Mccoy Rd", "city": "Centreville", "zip": "20121", "state": "VA" }, 

{  "address": "6455 Mccoy Rd", "city": "Centreville", "zip": "20121", "state": "VA" }, 

{  "address": "6405 Sutler Store Ct", "city": "Centreville", "zip": "20121", "state": "VA" }, 

{  "address": "3890 Fairfax Sq", "city": "Fairfax", "zip": "22031", "state": "VA" }, 

{  "address": "3890 Fairfax Sq", "city": "Fairfax", "zip": "22031", "state": "VA" }, 

{  "address": "2934 Piney Grove Ct", "city": "Fairfax", "zip": "22031", "state": "VA" }, 

{  "address": "2934 Piney Grove Ct", "city": "Fairfax", "zip": "22031", "state": "VA" }, 

{  "address": "9644 Blake Ln", "city": "Fairfax", "zip": "22031", "state": "VA" },

{  "address": "9644 Blake Ln", "city": "Fairfax", "zip": "22031", "state": "VA" }, 

{  "address": "3955 Persimmon Dr", "city": "Fairfax", "zip": "22031", "state": "VA" }, 

{  "address": "3955 Persimmon Dr", "city": "Fairfax", "zip": "22031", "state": "VA" }, 

{  "address": "10011 Laurie Pl", "city": "Fairfax", "zip": "22031", "state": "VA" }, 

{  "address": "10801 Rippon Lodge Dr", "city": "Fairfax", "zip": "22032", "state": "VA" }, 

{  "address": "10801 Rippon Lodge Dr", "city": "Fairfax", "zip": "22032", "state": "VA" }, 

{  "address": "4209 Middlebrook St", "city": "Fairfax", "zip": "22032", "state": "VA" }, 

{  "address": "4209 Middlebrook St", "city": "Fairfax", "zip": "22032", "state": "VA" }, 

{  "address": "4729 Briar Patch Ln", "city": "Fairfax", "zip": "22032", "state": "VA" }, 

{  "address": "4729 Briar Patch Ln", "city": "Fairfax", "zip": "22032", "state": "VA" }, 

{  "address": "10519 Earlham St", "city": "Fairfax", "zip": "22032", "state": "VA" },

{  "address": "10519 Earlham St", "city": "Fairfax", "zip": "22032", "state": "VA" }, 

{  "address": "4303 Argonne Dr", "city": "Fairfax", "zip": "22032", "state": "VA" }, 

{  "address": "12110 Monument Dr", "city": "Fairfax", "zip": "22033", "state": "VA" }, 

{  "address": "12110 Monument Dr", "city": "Fairfax", "zip": "22033", "state": "VA" }, 

{  "address": "12249 Pender Creek Cir", "city": "Fairfax", "zip": "22033", "state": "VA" }, 

{  "address": "12249 Pender Creek Cir", "city": "Fairfax", "zip": "22033", "state": "VA" }, 

{  "address": "12474 Sweet Leaf Ter", "city": "Fairfax", "zip": "22033", "state": "VA" },

{  "address": "12474 Sweet Leaf Ter", "city": "Fairfax", "zip": "22033", "state": "VA" }, 

{  "address": "12362 Washington Brice Rd", "city": "Fairfax", "zip": "22033", "state": "VA" }, 

{  "address": "12362 Washington Brice Rd", "city": "Fairfax", "zip": "22033", "state": "VA" }, 

{  "address": "3712 Broomsedge Ct", "city": "Fairfax", "zip": "22033", "state": "VA" }, 

{  "address": "8077 Genea Way #2", "city": "Falls Church", "zip": "22042", "state": "VA" }, 

{  "address": "7328 Poplar Ct", "city": "Falls Church", "zip": "22042", "state": "VA" }, 

{  "address": "2906 Meadow Ln", "city": "Falls Church", "zip": "22042", "state": "VA" }, 

{  "address": "2920 Woodlawn Ave", "city": "Falls Church", "zip": "22042", "state": "VA" }, 

{  "address": "6805 Kingwood Dr", "city": "Falls Church", "zip": "22042", "state": "VA" },

{  "address": "7756 New Providence Dr #14", "city": "Falls Church", "zip": "22042", "state": "VA" }, 

{  "address": "6913 Jefferson Ave", "city": "Falls Church", "zip": "22042", "state": "VA" }, 

{  "address": "6722 Chestnut Ave", "city": "Falls Church", "zip": "22042", "state": "VA" },

{  "address": "2833 Meadow Ln", "city": "Falls Church", "zip": "22042", "state": "VA" }, 

{  "address": "12802 Lady Fairfax Cir", "city": "Herndon", "zip": "20170", "state": "VA" }, 

{  "address": "12802 Lady Fairfax Cir", "city": "Herndon", "zip": "20170", "state": "VA" }, 

{  "address": "2165 Astoria Cir", "city": "Herndon", "zip": "20170", "state": "VA" }, 

{  "address": "2165 Astoria Cir", "city": "Herndon", "zip": "20170", "state": "VA" }, 

{  "address": "871 Grace St", "city": "Herndon", "zip": "20170", "state": "VA" }, 

{  "address": "871 Grace St", "city": "Herndon", "zip": "20170", "state": "VA" }, 

{  "address": "12119 Sandy Ct", "city": "Herndon", "zip": "20170", "state": "VA" }, 

{  "address": "12119 Sandy Ct", "city": "Herndon", "zip": "20170", "state": "VA" }, 

{  "address": "1102 Safa St", "city": "Herndon", "zip": "20170", "state": "VA" }, 

{  "address": "13450 Sunrise Valley Dr #100", "city": "Herndon", "zip": "20171", "state": "VA" }, 

{  "address": "13450 Sunrise Valley Dr #100", "city": "Herndon", "zip": "20171", "state": "VA" }, 

{  "address": "13568 Highland Mews Ct", "city": "Herndon", "zip": "20171", "state": "VA" }, 

{  "address": "13568 Highland Mews Ct", "city": "Herndon", "zip": "20171", "state": "VA" }, 

{  "address": "13792 Merrybrook Ct", "city": "Herndon", "zip": "20171", "state": "VA" }, 

{  "address": "13792 Merrybrook Ct", "city": "Herndon", "zip": "20171", "state": "VA" }, 

{  "address": "13792 Merrybrook Ct #APT 204", "city": "Herndon", "zip": "20171", "state": "VA" }, 

{  "address": "13792 Merrybrook Ct #APT 204", "city": "Herndon", "zip": "20171", "state": "VA" }, 

{  "address": "13958 Mansarde Ave", "city": "Herndon", "zip": "20171", "state": "VA" }, 

{  "address": "9769 Hagel Cir", "city": "Lorton", "zip": "22079", "state": "VA" }, 

{  "address": "8815 Lagrange St", "city": "Lorton", "zip": "22079", "state": "VA" }, 

{  "address": "9212 Treasure Oak Ct", "city": "Lorton", "zip": "22079", "state": "VA" }, 

{  "address": "11417 Potomac Rd", "city": "Lorton", "zip": "22079", "state": "VA" }, 

{  "address": "9034 Lorton Station Blvd #461", "city": "Lorton", "zip": "22079", "state": "VA" }, 

{  "address": "10718 Greene Dr", "city": "Lorton", "zip": "22079", "state": "VA" }, 

{  "address": "6713 Catskill Rd", "city": "Lorton", "zip": "22079", "state": "VA" }, 

{  "address": "7725 Porters Hill Ln", "city": "Lorton", "zip": "22079", "state": "VA" },

{  "address": "7309 Harrogate Ct", "city": "Lorton", "zip": "22079", "state": "VA" }, 

{  "address": "2342 Old Trail Dr", "city": "Reston", "zip": "20191", "state": "VA" }, 

{  "address": "2225 Wheelwright Ct", "city": "Reston", "zip": "20191", "state": "VA" }, 

{  "address": "2221 Stone Wheel Dr", "city": "Reston", "zip": "20191", "state": "VA" }, 

{  "address": "11571 Woodhollow Ct", "city": "Reston", "zip": "20191", "state": "VA" }, 

{  "address": "2367 Old Trail Dr", "city": "Reston", "zip": "20191", "state": "VA" }, 

{  "address": "11710 Decade Ct", "city": "Reston", "zip": "20191", "state": "VA" },

{  "address": "11439 Tanbark Dr", "city": "Reston", "zip": "20191", "state": "VA" }, 

{  "address": "2203 Halter Ln", "city": "Reston", "zip": "20191", "state": "VA" }, 

{  "address": "12222 Quorn Ln", "city": "Reston", "zip": "20191", "state": "VA" },

{  "address": "8704 Shadowlake Way", "city": "Springfield", "zip": "22153", "state": "VA" }, 

{  "address": "7404 Forest Hunt Ct", "city": "Springfield", "zip": "22153", "state": "VA" }, 

{  "address": "6914 Conservation Dr", "city": "Springfield", "zip": "22153", "state": "VA" }, 

{  "address": "7500 Ballyshannon Ct", "city": "Springfield", "zip": "22153", "state": "VA" }, 

{  "address": "8509 Jenner Ct", "city": "Springfield", "zip": "22153", "state": "VA" }, 

{  "address": "7404 Spring Tree Dr", "city": "Springfield", "zip": "22153", "state": "VA" }, 

{  "address": "8111 Loving Forest Ct", "city": "Springfield", "zip": "22153", "state": "VA" },

{  "address": "8015 Steeple Chase Ct", "city": "Springfield", "zip": "22153", "state": "VA" }, 

{  "address": "7684 Southern Oak Dr", "city": "Springfield", "zip": "22153", "state": "VA" }, 

{  "address": "10605 Mclean Ave", "city": "Fairfax", "zip": "22030", "state": "VA" }, 

{  "address": "10605 Mclean Ave", "city": "Fairfax", "zip": "22030", "state": "VA" }, 

{  "address": "5320 Hampton Way Frst", "city": "Fairfax", "zip": "22030", "state": "VA" }, 

{  "address": "5320 Hampton Way Frst", "city": "Fairfax", "zip": "22030", "state": "VA" }, 

{  "address": "3808 Egan Dr", "city": "Fairfax", "zip": "22030", "state": "VA" },

{  "address": "3808 Egan Dr", "city": "Fairfax", "zip": "22030", "state": "VA" }, 

{  "address": "12228 Lincoln Way Lk", "city": "Fairfax", "zip": "22030", "state": "VA" }, 

{  "address": "12228 Lincoln Way Lk", "city": "Fairfax", "zip": "22030", "state": "VA" },

{  "address": "4064 Clovet Dr", "city": "Fairfax", "zip": "22030", "state": "VA" }, 

{  "address": "44260 Navajo Dr", "city": "Ashburn", "zip": "20147", "state": "VA" }, 

{  "address": "44260 Navajo Dr", "city": "Ashburn", "zip": "20147", "state": "VA" }, 

{  "address": "44114 Gala Cir", "city": "Ashburn", "zip": "20147", "state": "VA" }, 

{  "address": "44114 Gala Cir", "city": "Ashburn", "zip": "20147", "state": "VA" }, 

{  "address": "20064 Coltsfoot Ter", "city": "Ashburn", "zip": "20147", "state": "VA" }, 

{  "address": "20064 Coltsfoot Ter", "city": "Ashburn", "zip": "20147", "state": "VA" }, 

{  "address": "44206 Big Trail Ter", "city": "Ashburn", "zip": "20147", "state": "VA" }, 

{  "address": "44206 Big Trail Ter", "city": "Ashburn", "zip": "20147", "state": "VA" }, 

{  "address": "43402 Postrail Sq", "city": "Ashburn", "zip": "20147", "state": "VA" }, 

{  "address": "21848 Ainsley Ct", "city": "Ashburn", "zip": "20148", "state": "VA" }, 

{  "address": "21848 Ainsley Ct", "city": "Ashburn", "zip": "20148", "state": "VA" }, 

{  "address": "43183 Thistledown Ter", "city": "Ashburn", "zip": "20148", "state": "VA" }, 

{  "address": "43183 Thistledown Ter", "city": "Ashburn", "zip": "20148", "state": "VA" }, 

{  "address": "42567 Good Hope Ln", "city": "Ashburn", "zip": "20148", "state": "VA" }, 

{  "address": "42567 Good Hope Ln", "city": "Ashburn", "zip": "20148", "state": "VA" },

{  "address": "21967 Shawbury Cir", "city": "Ashburn", "zip": "20148", "state": "VA" }, 

{  "address": "21967 Shawbury Cir", "city": "Ashburn", "zip": "20148", "state": "VA" }, 

{  "address": "22086 Avonworth Sq", "city": "Ashburn", "zip": "20148", "state": "VA" },

{  "address": "25946 Sarazen Dr", "city": "Chantilly", "zip": "20152", "state": "VA" }, 

{  "address": "25592 Upper Clubhouse Dr", "city": "Chantilly", "zip": "20152", "state": "VA" }, 

{  "address": "43715 Mink Meadows St", "city": "Chantilly", "zip": "20152", "state": "VA" }, 

{  "address": "43341 Royal Burkedale St", "city": "Chantilly", "zip": "20152", "state": "VA" }, 

{  "address": "25220 Lake Shore Sq #205", "city": "Chantilly", "zip": "20152", "state": "VA" },

{  "address": "43520 Emerald Ln", "city": "Chantilly", "zip": "20152", "state": "VA" }, 

{  "address": "43489 Interval St", "city": "Chantilly", "zip": "20152", "state": "VA" }, 

{  "address": "25941 Flintonbridge Dr", "city": "Chantilly", "zip": "20152", "state": "VA" }, 

{  "address": "43304 Jerpoint Ct", "city": "Chantilly", "zip": "20152", "state": "VA" },
{  "address": "195 Spencer Ter SE", "city": "Leesburg", "zip": "20175", "state": "VA" }, 

{  "address": "195 Spencer Ter SE", "city": "Leesburg", "zip": "20175", "state": "VA" }, 

{  "address": "651 Burnside Ter SE", "city": "Leesburg", "zip": "20175", "state": "VA" }, 

{  "address": "651 Burnside Ter SE", "city": "Leesburg", "zip": "20175", "state": "VA" }, 

{  "address": "129 Davis Ave SW", "city": "Leesburg", "zip": "20175", "state": "VA" }, 

{  "address": "129 Davis Ave SW", "city": "Leesburg", "zip": "20175", "state": "VA" }, 

{  "address": "508 Sunset View Ter SE", "city": "Leesburg", "zip": "20175", "state": "VA" }, 

{  "address": "508 Sunset View Ter SE", "city": "Leesburg", "zip": "20175", "state": "VA" }, 

{  "address": "108 Cagney Ter SE", "city": "Leesburg", "zip": "20175", "state": "VA" }, 

{  "address": "14572 Loyalty Rd", "city": "Leesburg", "zip": "20176", "state": "VA" }, 

{  "address": "14572 Loyalty Rd", "city": "Leesburg", "zip": "20176", "state": "VA" }, 

{  "address": "15905 Woolsthorpe Dr", "city": "Leesburg", "zip": "20176", "state": "VA" }, 

{  "address": "15905 Woolsthorpe Dr", "city": "Leesburg", "zip": "20176", "state": "VA" },

{  "address": "43932 Riverpoint Dr", "city": "Leesburg", "zip": "20176", "state": "VA" }, 

{  "address": "43932 Riverpoint Dr", "city": "Leesburg", "zip": "20176", "state": "VA" }, 

{  "address": "19026 Rocky Creek Dr", "city": "Leesburg", "zip": "20176", "state": "VA" }, 

{  "address": "19026 Rocky Creek Dr", "city": "Leesburg", "zip": "20176", "state": "VA" }, 

{  "address": "658 Ft Evans Rd NE", "city": "Leesburg", "zip": "20176", "state": "VA" }, 

{  "address": "806 N Watford St", "city": "Sterling", "zip": "20164", "state": "VA" }, 

{  "address": "806 N Watford St", "city": "Sterling", "zip": "20164", "state": "VA" }, 

{  "address": "712 Avondale Dr", "city": "Sterling", "zip": "20164", "state": "VA" }, 

{  "address": "712 Avondale Dr", "city": "Sterling", "zip": "20164", "state": "VA" }, 

{  "address": "218 Elizabeth Ct", "city": "Sterling", "zip": "20164", "state": "VA" }, 

{  "address": "218 Elizabeth Ct", "city": "Sterling", "zip": "20164", "state": "VA" },

{  "address": "46780 Southern Oaks Ter #T", "city": "Sterling", "zip": "20164", "state": "VA" }, 

{  "address": "46780 Southern Oaks Ter #T", "city": "Sterling", "zip": "20164", "state": "VA" }, 

{  "address": "46710 Bullfinch Sq", "city": "Sterling", "zip": "20164", "state": "VA" },

{  "address": "20935 Sandian Ter", "city": "Sterling", "zip": "20165", "state": "VA" }, 

{  "address": "20935 Sandian Ter", "city": "Sterling", "zip": "20165", "state": "VA" }, 

{  "address": "46509 Lynnhaven Sq", "city": "Sterling", "zip": "20165", "state": "VA" }, 

{  "address": "46509 Lynnhaven Sq", "city": "Sterling", "zip": "20165", "state": "VA" }, 

{  "address": "19385 Youngs Cliff Rd", "city": "Sterling", "zip": "20165", "state": "VA" }, 

{  "address": "19385 Youngs Cliff Rd", "city": "Sterling", "zip": "20165", "state": "VA" }, 

{  "address": "20315 Burnley Sq", "city": "Sterling", "zip": "20165", "state": "VA" }, 

{  "address": "20315 Burnley Sq", "city": "Sterling", "zip": "20165", "state": "VA" }, 

{  "address": "46671 Ashmere Sq", "city": "Sterling", "zip": "20165", "state": "VA" }, 

{  "address": "10151 Strawflower Ln", "city": "Manassas", "zip": "20110", "state": "VA" }, 

{  "address": "10151 Strawflower Ln", "city": "Manassas", "zip": "20110", "state": "VA" }, 

{  "address": "9901 Hawthorn Hill Ct", "city": "Manassas", "zip": "20110", "state": "VA" }, 

{  "address": "9901 Hawthorn Hill Ct", "city": "Manassas", "zip": "20110", "state": "VA" },

{  "address": "8418 Mckenzie Cir", "city": "Manassas", "zip": "20110", "state": "VA" }, 

{  "address": "8418 Mckenzie Cir", "city": "Manassas", "zip": "20110", "state": "VA" },

{  "address": "9429 Stonewall Rd", "city": "Manassas", "zip": "20110", "state": "VA" }, 

{  "address": "9429 Stonewall Rd", "city": "Manassas", "zip": "20110", "state": "VA" }, 

{  "address": "9004 Weir St", "city": "Manassas", "zip": "20110", "state": "VA" }, 

{  "address": "12027 Infantry Ln", "city": "Bristow", "zip": "20136", "state": "VA" }, 

{  "address": "8665 Horncastle Ct", "city": "Bristow", "zip": "20136", "state": "VA" }, 

{  "address": "13736 Denham Way", "city": "Bristow", "zip": "20136", "state": "VA" }, 

{  "address": "12530 Haltwhistle Ct", "city": "Bristow", "zip": "20136", "state": "VA" }, 

{  "address": "13519 Grouserun Ln", "city": "Bristow", "zip": "20136", "state": "VA" }, 

{  "address": "11914 Benton Lake Rd", "city": "Bristow", "zip": "20136", "state": "VA" }, 

{  "address": "8622 Ellesmere Way", "city": "Bristow", "zip": "20136", "state": "VA" },

{  "address": "13472 Wansteadt Pl", "city": "Bristow", "zip": "20136", "state": "VA" }, 

{  "address": "9305 Branch Park Trl", "city": "Bristow", "zip": "20136", "state": "VA" }, 

{  "address": "6372 E Pdgrims Rest Rd", "city": "Gainesville", "zip": "20155", "state": "VA" }, 

{  "address": "17683 Glass Ridge Pl", "city": "Gainesville", "zip": "20155", "state": "VA" }, 

{  "address": "7208 Bladen Pl", "city": "Gainesville", "zip": "20155", "state": "VA" }, 

{  "address": "7007 Little Thames Dr", "city": "Gainesville", "zip": "20155", "state": "VA" },

{  "address": "8005 Tysons Oaks Ct", "city": "Gainesville", "zip": "20155", "state": "VA" }, 

{  "address": "13550 Heathcote Blvd", "city": "Gainesville", "zip": "20155", "state": "VA" }, 

{  "address": "14741 Deming Dr", "city": "Gainesville", "zip": "20155", "state": "VA" }, 

{  "address": "13859 Crabtree Way", "city": "Gainesville", "zip": "20155", "state": "VA" }, 

{  "address": "15698 Spyglass Hill Loop", "city": "Gainesville", "zip": "20155", "state": "VA" },

{  "address": "8835 Morrisania Mews", "city": "Manassas", "zip": "20109", "state": "VA" }, 

{  "address": "8835 Morrisania Mews", "city": "Manassas", "zip": "20109", "state": "VA" }, 

{  "address": "8042 Portwood Turn", "city": "Manassas", "zip": "20109", "state": "VA" }, 

{  "address": "8042 Portwood Turn", "city": "Manassas", "zip": "20109", "state": "VA" },

{  "address": "10489 Butterfield St", "city": "Manassas", "zip": "20109", "state": "VA" }, 

{  "address": "10489 Butterfield St", "city": "Manassas", "zip": "20109", "state": "VA" },

{  "address": "7824 Flager Cir", "city": "Manassas", "zip": "20109", "state": "VA" }, 

{  "address": "7824 Flager Cir", "city": "Manassas", "zip": "20109", "state": "VA" },

{  "address": "10019 Copeland Dr", "city": "Manassas", "zip": "20109", "state": "VA" }, 

{  "address": "9216 Matthew Dr", "city": "Manassas", "zip": "20111", "state": "VA" }, 

{  "address": "9216 Matthew Dr", "city": "Manassas", "zip": "20111", "state": "VA" }, 

{  "address": "7988 Blooms Rd", "city": "Manassas", "zip": "20111", "state": "VA" }, 

{  "address": "7988 Blooms Rd", "city": "Manassas", "zip": "20111", "state": "VA" }, 

{  "address": "8136 Rainwater Cir", "city": "Manassas", "zip": "20111", "state": "VA" }, 

{  "address": "8136 Rainwater Cir", "city": "Manassas", "zip": "20111", "state": "VA" },

{  "address": "6405 Yates Ford Rd", "city": "Manassas", "zip": "20111", "state": "VA" }, 

{  "address": "6405 Yates Ford Rd", "city": "Manassas", "zip": "20111", "state": "VA" },

{  "address": "7016 Bruin Ct", "city": "Manassas", "zip": "20111", "state": "VA" }, 

{  "address": "13462 Lock Loop", "city": "Woodbridge", "zip": "22192", "state": "VA" }, 

{  "address": "13462 Lock Loop", "city": "Woodbridge", "zip": "22192", "state": "VA" }, 

{  "address": "12909 Titania Way", "city": "Woodbridge", "zip": "22192", "state": "VA" }, 

{  "address": "12909 Titania Way", "city": "Woodbridge", "zip": "22192", "state": "VA" }, 

{  "address": "12453 Cavalier Dr", "city": "Woodbridge", "zip": "22192", "state": "VA" },

{  "address": "12453 Cavalier Dr", "city": "Woodbridge", "zip": "22192", "state": "VA" }, 

{  "address": "2932 Madeira Ct", "city": "Woodbridge", "zip": "22192", "state": "VA" }, 

{  "address": "2932 Madeira Ct", "city": "Woodbridge", "zip": "22192", "state": "VA" },

{  "address": "12703 Lotte Dr", "city": "Woodbridge", "zip": "22192", "state": "VA" }, 

{  "address": "13338 Paramount Ln", "city": "Woodbridge", "zip": "22193", "state": "VA" }, 

{  "address": "13338 Paramount Ln", "city": "Woodbridge", "zip": "22193", "state": "VA" }, 

{  "address": "13721 Greenbriar Dr", "city": "Woodbridge", "zip": "22193", "state": "VA" }, 

{  "address": "13721 Greenbriar Dr", "city": "Woodbridge", "zip": "22193", "state": "VA" },

{  "address": "13358 Pocono Ct", "city": "Woodbridge", "zip": "22193", "state": "VA" }, 

{  "address": "13358 Pocono Ct", "city": "Woodbridge", "zip": "22193", "state": "VA" }, 

{  "address": "3474 Beale Ct", "city": "Woodbridge", "zip": "22193", "state": "VA" }, 

{  "address": "3474 Beale Ct", "city": "Woodbridge", "zip": "22193", "state": "VA" }, 

{  "address": "4370 Welsh Ln", "city": "Woodbridge", "zip": "22193", "state": "VA" }, 

{  "address": "12218 Corter Ave", "city": "Fredericksburg", "zip": "22407", "state": "VA" }, 

{  "address": "12218 Corter Ave", "city": "Fredericksburg", "zip": "22407", "state": "VA" }, 

{  "address": "12218 Corter Ave", "city": "Fredericksburg", "zip": "22407", "state": "VA" }, 

{  "address": "12218 Corter Ave", "city": "Fredericksburg", "zip": "22407", "state": "VA" }, 

{  "address": "12305 Glade Dr", "city": "Fredericksburg", "zip": "22407", "state": "VA" },

{  "address": "12305 Glade Dr", "city": "Fredericksburg", "zip": "22407", "state": "VA" }, 

{  "address": "5400 S Branch Rd", "city": "Fredericksburg", "zip": "22407", "state": "VA" }, 

{  "address": "5400 S Branch Rd", "city": "Fredericksburg", "zip": "22407", "state": "VA" },

{  "address": "10606 Wakeman Dr", "city": "Fredericksburg", "zip": "22407", "state": "VA" }, 

{  "address": "10524 Coles Ln", "city": "Fredericksburg", "zip": "22408", "state": "VA" }, 

{  "address": "10524 Coles Ln", "city": "Fredericksburg", "zip": "22408", "state": "VA" }, 

{  "address": "8810 New Castle Ct", "city": "Fredericksburg", "zip": "22408", "state": "VA" },

{  "address": "8810 New Castle Ct", "city": "Fredericksburg", "zip": "22408", "state": "VA" }, 

{  "address": "7900 S Woods Dr", "city": "Fredericksburg", "zip": "22408", "state": "VA" }, 

{  "address": "7900 S Woods Dr", "city": "Fredericksburg", "zip": "22408", "state": "VA" },

{  "address": "3815 Chapman Dr", "city": "Fredericksburg", "zip": "22408", "state": "VA" }, 

{  "address": "3815 Chapman Dr", "city": "Fredericksburg", "zip": "22408", "state": "VA" }, 

{  "address": "4719 River Crest Ct", "city": "Fredericksburg", "zip": "22408", "state": "VA" }, 
{  "address": "522 Ferry Rd", "city": "Fredericksburg", "zip": "22405", "state": "VA" }, 

{  "address": "522 Ferry Rd", "city": "Fredericksburg", "zip": "22405", "state": "VA" }, 

{  "address": "20 Brentwood Ln", "city": "Fredericksburg", "zip": "22405", "state": "VA" }, 

{  "address": "20 Brentwood Ln", "city": "Fredericksburg", "zip": "22405", "state": "VA" },

{  "address": "7 Myers Dr", "city": "Fredericksburg", "zip": "22405", "state": "VA" }, 

{  "address": "7 Myers Dr", "city": "Fredericksburg", "zip": "22405", "state": "VA" }, 

{  "address": "43 Willow Branch Pl", "city": "Fredericksburg", "zip": "22405", "state": "VA" }, 

{  "address": "43 Willow Branch Pl", "city": "Fredericksburg", "zip": "22405", "state": "VA" }, 

{  "address": "507 Jett St", "city": "Fredericksburg", "zip": "22405", "state": "VA" }, 

{  "address": "14 Bridgeport Cir", "city": "Stafford", "zip": "22554", "state": "VA" }, 

{  "address": "14 Bridgeport Cir", "city": "Stafford", "zip": "22554", "state": "VA" }, 

{  "address": "217 Willow Landing Rd #1", "city": "Stafford", "zip": "22554", "state": "VA" }, 

{  "address": "217 Willow Landing Rd #1", "city": "Stafford", "zip": "22554", "state": "VA" },

{  "address": "65 Stonegate Pl", "city": "Stafford", "zip": "22554", "state": "VA" }, 

{  "address": "65 Stonegate Pl", "city": "Stafford", "zip": "22554", "state": "VA" },

{  "address": "78 Acadia St", "city": "Stafford", "zip": "22554", "state": "VA" }, 

{  "address": "78 Acadia St", "city": "Stafford", "zip": "22554", "state": "VA" }, 

{  "address": "58 Sentinel Ridge Ln", "city": "Stafford", "zip": "22554", "state": "VA" }, 

{  "address": "652 Mountain Heights Rd", "city": "Front Royal", "zip": "22630", "state": "VA" }, 

{  "address": "293 Crooked Run Rd", "city": "Front Royal", "zip": "22630", "state": "VA" }, 

{  "address": "967 High Knob Rd", "city": "Front Royal", "zip": "22630", "state": "VA" }, 

{  "address": "64 Tara Rd", "city": "Front Royal", "zip": "22630", "state": "VA" }, 

{  "address": "311 Lee St", "city": "Front Royal", "zip": "22630", "state": "VA" }, 

{  "address": "2799 Rivermont Dr", "city": "Front Royal", "zip": "22630", "state": "VA" }, 

{  "address": "303 Blue Ridge Ave", "city": "Front Royal", "zip": "22630", "state": "VA" },

{  "address": "219 Midway Ave", "city": "Front Royal", "zip": "22630", "state": "VA" }, 

{  "address": "117 Washington Ave", "city": "Front Royal", "zip": "22630", "state": "VA" }, 

{  "address": "104 Williamson Rd", "city": "Winchester", "zip": "22602", "state": "VA" }, 

{  "address": "111 Kinross Dr", "city": "Winchester", "zip": "22602", "state": "VA" }, 

{  "address": "112 Huntcrest Cir", "city": "Winchester", "zip": "22602", "state": "VA" }, 

{  "address": "106 Stanley Cir", "city": "Winchester", "zip": "22602", "state": "VA" }, 

{  "address": "137 Orchard Dr", "city": "Winchester", "zip": "22602", "state": "VA" }, 

{  "address": "111 Abbey Rd", "city": "Winchester", "zip": "22602", "state": "VA" }, 

{  "address": "540 Laurelwood Dr", "city": "Winchester", "zip": "22602", "state": "VA" }, 

{  "address": "160 Stuart Dr", "city": "Winchester", "zip": "22602", "state": "VA" }, 

{  "address": "204 Rosewood Ln", "city": "Winchester", "zip": "22602", "state": "VA" }, 

{  "address": "2304 Maplewood Dr", "city": "Culpeper", "zip": "22701", "state": "VA" }, 

{  "address": "8049 Kirtley Trl", "city": "Culpeper", "zip": "22701", "state": "VA" }, 

{  "address": "7292 James Monroe Hwy", "city": "Culpeper", "zip": "22701", "state": "VA" }, 

{  "address": "8436 Kirtley Trl", "city": "Culpeper", "zip": "22701", "state": "VA" }, 

{  "address": "3915 Thoroughfare Rd", "city": "Culpeper", "zip": "22701", "state": "VA" }, 

{  "address": "6357 Glebe Way", "city": "Culpeper", "zip": "22701", "state": "VA" }, 

{  "address": "7490 Kirtley Trl", "city": "Culpeper", "zip": "22701", "state": "VA" }, 

{  "address": "17289 N Merrimac Rd", "city": "Culpeper", "zip": "22701", "state": "VA" }, 

{  "address": "6211 Glebe Way", "city": "Culpeper", "zip": "22701", "state": "VA" },

{  "address": "319 N Mill Rd", "city": "Salem", "zip": "24153", "state": "VA" }, 

{  "address": "912 Gatling Ln", "city": "Salem", "zip": "24153", "state": "VA" }, 

{  "address": "1945 Roanoke Blvd", "city": "Salem", "zip": "24153", "state": "VA" }, 

{  "address": "1501 Ashley Dr", "city": "Salem", "zip": "24153", "state": "VA" }, 

{  "address": "729 Florida St", "city": "Salem", "zip": "24153", "state": "VA" },

{  "address": "622 Cleveland Ave", "city": "Salem", "zip": "24153", "state": "VA" }, 

{  "address": "5164 Glenvar Heights Blvd", "city": "Salem", "zip": "24153", "state": "VA" }, 

{  "address": "4710 Lake Front Dr", "city": "Salem", "zip": "24153", "state": "VA" }, 

{  "address": "5007 Bradshaw Rd", "city": "Salem", "zip": "24153", "state": "VA" },

{  "address": "2670 Barrenridge Rd", "city": "Staunton", "zip": "24401", "state": "VA" }, 

{  "address": "47 Seymour Cir", "city": "Staunton", "zip": "24401", "state": "VA" }, 

{  "address": "3002 Old Greenville Rd", "city": "Staunton", "zip": "24401", "state": "VA" }, 

{  "address": "2850 Old Greenville Rd", "city": "Staunton", "zip": "24401", "state": "VA" }, 

{  "address": "180 Howardsville Rd", "city": "Staunton", "zip": "24401", "state": "VA" }, 

{  "address": "1170 Stuarts Draft Hwy", "city": "Staunton", "zip": "24401", "state": "VA" }, 

{  "address": "2028 Old Greenville Rd", "city": "Staunton", "zip": "24401", "state": "VA" }, 

{  "address": "2723 Lee Jackson Hwy", "city": "Staunton", "zip": "24401", "state": "VA" },

{  "address": "438 Chestnut Ridge Rd", "city": "Staunton", "zip": "24401", "state": "VA" }, 

{  "address": "540 Hamlet Ave #3", "city": "Waynesboro", "zip": "22980", "state": "VA" }, 

{  "address": "776 E Side Hwy", "city": "Waynesboro", "zip": "22980", "state": "VA" }, 

{  "address": "14 Brook Cir", "city": "Waynesboro", "zip": "22980", "state": "VA" }, 

{  "address": "1220 3rd St", "city": "Waynesboro", "zip": "22980", "state": "VA" }, 

{  "address": "586 N Bath Ave", "city": "Waynesboro", "zip": "22980", "state": "VA" }, 

{  "address": "33 Farmside St", "city": "Waynesboro", "zip": "22980", "state": "VA" },

{  "address": "1272 Jefferson Hwy", "city": "Fishersville", "zip": "22980", "state": "VA" }, 

{  "address": "29 Heatwole Dr", "city": "Waynesboro", "zip": "22980", "state": "VA" }, 

{  "address": "57 Thomas Dr", "city": "Waynesboro", "zip": "22980", "state": "VA" }, 

{  "address": "146 Brandywine Ct", "city": "Charlottesville", "zip": "22901", "state": "VA" }, 

{  "address": "1185 Owensville Rd", "city": "Charlottesville", "zip": "22901", "state": "VA" }, 

{  "address": "134 Hessian Hills Way #APT 1", "city": "Charlottesville", "zip": "22901", "state": "VA" }, 

{  "address": "1160 Tennis Rd", "city": "Charlottesville", "zip": "22901", "state": "VA" }, 

{  "address": "1006 Park St", "city": "Charlottesville", "zip": "22901", "state": "VA" }, 

{  "address": "1025 Cottonwood Rd", "city": "Charlottesville", "zip": "22901", "state": "VA" }, 

{  "address": "1201 Lili Ln", "city": "Charlottesville", "zip": "22901", "state": "VA" }, 

{  "address": "3070 Morewood Ln", "city": "Charlottesville", "zip": "22901", "state": "VA" },

{  "address": "170 Georgetown Rd #A", "city": "Charlottesville", "zip": "22901", "state": "VA" }, 

{  "address": "Po Box 3668", "city": "Charlottesville", "zip": "22903", "state": "VA" }, 

{  "address": "810 Page St", "city": "Charlottesville", "zip": "22903", "state": "VA" }, 

{  "address": "201 Holly Dr", "city": "Charlottesville", "zip": "22903", "state": "VA" }, 

{  "address": "255 Colonnade Dr #34", "city": "Charlottesville", "zip": "22903", "state": "VA" }, 

{  "address": "163 Chancellor St", "city": "Charlottesville", "zip": "22903", "state": "VA" }, 

{  "address": "802 Cynthianna Ave", "city": "Charlottesville", "zip": "22903", "state": "VA" }, 

{  "address": "810 Fendall Ter", "city": "Charlottesville", "zip": "22903", "state": "VA" },

{  "address": "267 Turkey Ridge Rd", "city": "Charlottesville", "zip": "22903", "state": "VA" }, 

{  "address": "834 Village Rd", "city": "Charlottesville", "zip": "22903", "state": "VA" }, 

{  "address": "6056 Mount Cross Rd", "city": "Danville", "zip": "24540", "state": "VA" }, 

{  "address": "4009 Pittwood Dr", "city": "Danville", "zip": "24540", "state": "VA" }, 

{  "address": "3566 R And L Smith Dr", "city": "Danville", "zip": "24540", "state": "VA" }, 

{  "address": "133 Dakota Dr", "city": "Danville", "zip": "24540", "state": "VA" }, 

{  "address": "642 Arnett Blvd", "city": "Danville", "zip": "24540", "state": "VA" },

{  "address": "308 Briarwood Dr", "city": "Danville", "zip": "24540", "state": "VA" }, 

{  "address": "209 Willow St", "city": "Danville", "zip": "24540", "state": "VA" }, 

{  "address": "185 Alpine Dr", "city": "Danville", "zip": "24540", "state": "VA" }, 

{  "address": "301 Bellevue St", "city": "Danville", "zip": "24540", "state": "VA" }, 

{  "address": "3277 Preston Shore Dr", "city": "Harrisonburg", "zip": "22801", "state": "VA" }, 

{  "address": "2001 Pine Harbor Ln", "city": "Harrisonburg", "zip": "22801", "state": "VA" }, 

{  "address": "1395 Stockings Cir", "city": "Harrisonburg", "zip": "22801", "state": "VA" }, 

{  "address": "3516 Shen Lake Dr", "city": "Harrisonburg", "zip": "22801", "state": "VA" }, 

{  "address": "2511 Ramblewood Rd", "city": "Harrisonburg", "zip": "22801", "state": "VA" },

{  "address": "3346 Clement Dr", "city": "Harrisonburg", "zip": "22801", "state": "VA" }, 

{  "address": "1372 Hunters Rd", "city": "Harrisonburg", "zip": "22801", "state": "VA" }, 

{  "address": "10 Holly Ct", "city": "Harrisonburg", "zip": "22801", "state": "VA" },

{  "address": "2200 Ridgedale Rd", "city": "Harrisonburg", "zip": "22801", "state": "VA" }, 

{  "address": "2293 Keezletown Rd", "city": "Harrisonburg", "zip": "22802", "state": "VA" }, 

{  "address": "1641 Park Rd #B", "city": "Harrisonburg", "zip": "22802", "state": "VA" }, 

{  "address": "475 Lacey Spring Rd", "city": "Harrisonburg", "zip": "22802", "state": "VA" }, 

{  "address": "497 Gravels Rd", "city": "Harrisonburg", "zip": "22802", "state": "VA" }, 

{  "address": "566 Viewmont Ct", "city": "Harrisonburg", "zip": "22802", "state": "VA" }, 

{  "address": "685 Gailcrist Dr", "city": "Harrisonburg", "zip": "22802", "state": "VA" }, 

{  "address": "324 Kelley St", "city": "Harrisonburg", "zip": "22802", "state": "VA" },

{  "address": "831 Pheasant Ct", "city": "Harrisonburg", "zip": "22802", "state": "VA" }, 

{  "address": "3322 Noland Dr", "city": "Harrisonburg", "zip": "22802", "state": "VA" }, 

{  "address": "411 Robin Dr", "city": "Lynchburg", "zip": "24502", "state": "VA" }, 

{  "address": "4536 Greenwood Dr", "city": "Lynchburg", "zip": "24502", "state": "VA" }, 

{  "address": "110 Gatlin St", "city": "Lynchburg", "zip": "24502", "state": "VA" }, 

{  "address": "1714 Danbury Dr", "city": "Lynchburg", "zip": "24502", "state": "VA" }, 

{  "address": "6128 Pawnee Dr", "city": "Lynchburg", "zip": "24502", "state": "VA" },

{  "address": "503 Westview Dr", "city": "Lynchburg", "zip": "24502", "state": "VA" }, 

{  "address": "15 Mountain View Dr", "city": "Lynchburg", "zip": "24502", "state": "VA" },

{  "address": "1552 Knott St", "city": "Lynchburg", "zip": "24502", "state": "VA" }, 

{  "address": "7133 Suncrest Dr", "city": "Lynchburg", "zip": "24502", "state": "VA" }, 
{  "address": "13518 Evelyn Dr", "city": "Chester", "zip": "23831", "state": "VA" }, 

{  "address": "4050 Way Crk", "city": "Chester", "zip": "23831", "state": "VA" }, 

{  "address": "12709 Richmond St", "city": "Chester", "zip": "23831", "state": "VA" }, 

{  "address": "15121 Broadwater Way", "city": "Chester", "zip": "23831", "state": "VA" },

{  "address": "15351 Timsberry Cir", "city": "Chester", "zip": "23831", "state": "VA" }, 

{  "address": "3124 Poplar View Pl", "city": "Chester", "zip": "23831", "state": "VA" },

{  "address": "14401 Tooley Ter", "city": "Chester", "zip": "23831", "state": "VA" }, 

{  "address": "11501 Marsden Rd", "city": "Chester", "zip": "23831", "state": "VA" }, 

{  "address": "11913 Quiet Pine Dr", "city": "Chester", "zip": "23831", "state": "VA" }, 

{  "address": "7300 Cogbill Rd", "city": "Chesterfield", "zip": "23832", "state": "VA" }, 

{  "address": "5619 Kings Grove Dr", "city": "Chesterfield", "zip": "23832", "state": "VA" }, 

{  "address": "6511 Licking Creek Dr", "city": "Chesterfield", "zip": "23832", "state": "VA" }, 

{  "address": "5515 Townsbury Ter", "city": "Chesterfield", "zip": "23832", "state": "VA" },

{  "address": "9910 Breslin Dr", "city": "Chesterfield", "zip": "23832", "state": "VA" }, 

{  "address": "5510 Newbys Bridge Rd", "city": "Chesterfield", "zip": "23832", "state": "VA" }, 

{  "address": "6829 Silliman Dr", "city": "Chesterfield", "zip": "23832", "state": "VA" }, 

{  "address": "4006 West Ter", "city": "Chesterfield", "zip": "23832", "state": "VA" },

{  "address": "3918 Round Hill Ct", "city": "Chesterfield", "zip": "23832", "state": "VA" }, 

{  "address": "3310 Nuttree Woods Pl", "city": "Midlothian", "zip": "23112", "state": "VA" }, 

{  "address": "3310 Nuttree Woods Pl", "city": "Midlothian", "zip": "23112", "state": "VA" }, 

{  "address": "4121 Mallard Landing Cir", "city": "Midlothian", "zip": "23112", "state": "VA" }, 

{  "address": "4121 Mallard Landing Cir", "city": "Midlothian", "zip": "23112", "state": "VA" },

{  "address": "11912 Chislet Ct", "city": "Midlothian", "zip": "23112", "state": "VA" }, 

{  "address": "11912 Chislet Ct", "city": "Midlothian", "zip": "23112", "state": "VA" }, 

{  "address": "15105 Watermill Lake Trl", "city": "Midlothian", "zip": "23112", "state": "VA" }, 

{  "address": "15105 Watermill Lake Trl", "city": "Midlothian", "zip": "23112", "state": "VA" },

{  "address": "3606 Pencader Rd", "city": "Midlothian", "zip": "23112", "state": "VA" }, 

{  "address": "2505 Atwell Dr", "city": "Richmond", "zip": "23234", "state": "VA" }, 

{  "address": "2505 Atwell Dr", "city": "Richmond", "zip": "23234", "state": "VA" }, 

{  "address": "3318 Mike Rd", "city": "Richmond", "zip": "23234", "state": "VA" }, 

{  "address": "3318 Mike Rd", "city": "Richmond", "zip": "23234", "state": "VA" },

{  "address": "4016 Bingham Dr", "city": "Richmond", "zip": "23234", "state": "VA" },

{  "address": "4016 Bingham Dr", "city": "Richmond", "zip": "23234", "state": "VA" }, 

{  "address": "6225 Dorius Dr", "city": "Richmond", "zip": "23234", "state": "VA" }, 

{  "address": "6225 Dorius Dr", "city": "Richmond", "zip": "23234", "state": "VA" },

{  "address": "6801 Beulah Oaks Ln", "city": "Richmond", "zip": "23234", "state": "VA" }, 

{  "address": "8311 Soft Wind Dr", "city": "Mechanicsville", "zip": "23111", "state": "VA" }, 

{  "address": "8311 Soft Wind Dr", "city": "Mechanicsville", "zip": "23111", "state": "VA" }, 

{  "address": "7167 Mill Valley Rd", "city": "Mechanicsville", "zip": "23111", "state": "VA" }, 

{  "address": "7167 Mill Valley Rd", "city": "Mechanicsville", "zip": "23111", "state": "VA" }, 

{  "address": "6139 Stockade Ct", "city": "Mechanicsville", "zip": "23111", "state": "VA" }, 

{  "address": "6139 Stockade Ct", "city": "Mechanicsville", "zip": "23111", "state": "VA" }, 

{  "address": "6100 Perryville Dr", "city": "Mechanicsville", "zip": "23111", "state": "VA" },

{  "address": "6100 Perryville Dr", "city": "Mechanicsville", "zip": "23111", "state": "VA" }, 

{  "address": "6767 Cold Harbor Rd", "city": "Mechanicsville", "zip": "23111", "state": "VA" }, 

{  "address": "9163 Hunters Chase Ct", "city": "Mechanicsville", "zip": "23116", "state": "VA" }, 

{  "address": "9163 Hunters Chase Ct", "city": "Mechanicsville", "zip": "23116", "state": "VA" }, 

{  "address": "9108 Minglewood Ln", "city": "Mechanicsville", "zip": "23116", "state": "VA" }, 

{  "address": "9108 Minglewood Ln", "city": "Mechanicsville", "zip": "23116", "state": "VA" }, 

{  "address": "9405 Apple Blossom Dr", "city": "Mechanicsville", "zip": "23116", "state": "VA" }, 

{  "address": "9405 Apple Blossom Dr", "city": "Mechanicsville", "zip": "23116", "state": "VA" },

{  "address": "9080 Winterham Dr", "city": "Mechanicsville", "zip": "23116", "state": "VA" }, 

{  "address": "9080 Winterham Dr", "city": "Mechanicsville", "zip": "23116", "state": "VA" }, 

{  "address": "8093 Crown Colony Pky", "city": "Mechanicsville", "zip": "23116", "state": "VA" },

{  "address": "4017 Riverplace Ter", "city": "Glen Allen", "zip": "23059", "state": "VA" }, 

{  "address": "11003 Winfrey Rd", "city": "Glen Allen", "zip": "23059", "state": "VA" }, 

{  "address": "10516 Runnymeade Dr", "city": "Glen Allen", "zip": "23059", "state": "VA" }, 

{  "address": "3117 Stone Arbor Ln", "city": "Glen Allen", "zip": "23059", "state": "VA" }, 

{  "address": "5909 Chapel Lawn Ter", "city": "Glen Allen", "zip": "23059", "state": "VA" }, 

{  "address": "11633 Sethwarner Dr", "city": "Glen Allen", "zip": "23059", "state": "VA" }, 

{  "address": "11919 Park Way Frst", "city": "Glen Allen", "zip": "23059", "state": "VA" }, 

{  "address": "4916 Grey Oaks Villas Dr", "city": "Glen Allen", "zip": "23059", "state": "VA" },

{  "address": "12422 Greenwich Dr", "city": "Glen Allen", "zip": "23059", "state": "VA" }, 

{  "address": "9609 Fireside Dr", "city": "Glen Allen", "zip": "23060", "state": "VA" }, 

{  "address": "2104 Megan Dr", "city": "Glen Allen", "zip": "23060", "state": "VA" }, 

{  "address": "8017 Nicewood Rd", "city": "Glen Allen", "zip": "23060", "state": "VA" }, 

{  "address": "2800 Lito Rd", "city": "Glen Allen", "zip": "23060", "state": "VA" }, 

{  "address": "9532 Kennedy Station Ter", "city": "Glen Allen", "zip": "23060", "state": "VA" },

{  "address": "1907 Brilland Ct", "city": "Glen Allen", "zip": "23060", "state": "VA" }, 

{  "address": "804 Stonemeadow Dr", "city": "Glen Allen", "zip": "23060", "state": "VA" }, 

{  "address": "1060 Telegraph Station Ln", "city": "Glen Allen", "zip": "23060", "state": "VA" },

{  "address": "2520 Woodman Trace Dr", "city": "Glen Allen", "zip": "23060", "state": "VA" }, 

{  "address": "2001 Hungary Rd", "city": "Richmond", "zip": "23228", "state": "VA" }, 

{  "address": "2001 Hungary Rd", "city": "Richmond", "zip": "23228", "state": "VA" }, 

{  "address": "8611 Woodman Rd", "city": "Richmond", "zip": "23228", "state": "VA" }, 

{  "address": "7105 Fernwood St", "city": "Richmond", "zip": "23228", "state": "VA" }, 

{  "address": "3305 Webb Rd", "city": "Richmond", "zip": "23228", "state": "VA" }, 

{  "address": "2605 Waldo Ln", "city": "Richmond", "zip": "23228", "state": "VA" }, 

{  "address": "1 Gateway E", "city": "Richmond", "zip": "23229", "state": "VA" }, 

{  "address": "1 Gateway E", "city": "Richmond", "zip": "23229", "state": "VA" }, 

{  "address": "7710 Rock Creek Rd", "city": "Richmond", "zip": "23229", "state": "VA" }, 

{  "address": "7710 Rock Creek Rd", "city": "Richmond", "zip": "23229", "state": "VA" },

{  "address": "1023 Ridge Top Rd", "city": "Richmond", "zip": "23229", "state": "VA" }, 

{  "address": "1023 Ridge Top Rd", "city": "Richmond", "zip": "23229", "state": "VA" },

{  "address": "8715 Avalon Dr", "city": "Richmond", "zip": "23229", "state": "VA" }, 

{  "address": "8715 Avalon Dr", "city": "Richmond", "zip": "23229", "state": "VA" },

{  "address": "9414 Sir Barry Ct", "city": "Richmond", "zip": "23229", "state": "VA" }, 

{  "address": "1614 Thalia Cres", "city": "Richmond", "zip": "23231", "state": "VA" }, 

{  "address": "1614 Thalia Cres", "city": "Richmond", "zip": "23231", "state": "VA" }, 

{  "address": "1362 Jennie Scher Rd #G", "city": "Richmond", "zip": "23231", "state": "VA" }, 

{  "address": "1362 Jennie Scher Rd #G", "city": "Richmond", "zip": "23231", "state": "VA" }, 

{  "address": "4625 Jennell Crescent Ct", "city": "Richmond", "zip": "23231", "state": "VA" },

{  "address": "4625 Jennell Crescent Ct", "city": "Richmond", "zip": "23231", "state": "VA" }, 

{  "address": "1370 Freshet Ct", "city": "Richmond", "zip": "23231", "state": "VA" }, 

{  "address": "1370 Freshet Ct", "city": "Richmond", "zip": "23231", "state": "VA" }, 

{  "address": "4632 Grand Ledge Ct", "city": "Richmond", "zip": "23231", "state": "VA" },

{  "address": "3501 Chesterbrook Ct", "city": "Richmond", "zip": "23233", "state": "VA" }, 

{  "address": "3501 Chesterbrook Ct", "city": "Richmond", "zip": "23233", "state": "VA" }, 

{  "address": "1315 S 1st Ave", "city": "Hopewell", "zip": "23860", "state": "VA" }, 

{  "address": "1520 Piper Square Dr #APT H", "city": "Hopewell", "zip": "23860", "state": "VA" }, 

{  "address": "3000 Belmont Ave", "city": "Hopewell", "zip": "23860", "state": "VA" }, 

{  "address": "1605 W City Point Rd", "city": "Hopewell", "zip": "23860", "state": "VA" }, 

{  "address": "316 Brown Ave", "city": "Hopewell", "zip": "23860", "state": "VA" }, 

{  "address": "4919 Old Woodlawn St", "city": "Hopewell", "zip": "23860", "state": "VA" },

{  "address": "407 Stone Hearth Ct", "city": "Hopewell", "zip": "23860", "state": "VA" }, 

{  "address": "3307 Freeman St", "city": "Hopewell", "zip": "23860", "state": "VA" }, 

{  "address": "505 N 4th Ave", "city": "Hopewell", "zip": "23860", "state": "VA" },

{  "address": "235 Terrace Ave", "city": "Petersburg", "zip": "23803", "state": "VA" }, 

{  "address": "20221 Eagle Cove Ct", "city": "Petersburg", "zip": "23803", "state": "VA" }, 

{  "address": "19905 Matoaca Rd", "city": "Petersburg", "zip": "23803", "state": "VA" }, 

{  "address": "1128 Pointer St", "city": "Petersburg", "zip": "23803", "state": "VA" },

{  "address": "21403 Deodora Dr", "city": "Petersburg", "zip": "23803", "state": "VA" }, 

{  "address": "20407 Williams St", "city": "Petersburg", "zip": "23803", "state": "VA" }, 

{  "address": "14719 Grand Forest Ct", "city": "Petersburg", "zip": "23803", "state": "VA" }, 

{  "address": "1020 Ruffin Mill Pl", "city": "Petersburg", "zip": "23803", "state": "VA" }, 

{  "address": "5954 Ferintosh Ln", "city": "Petersburg", "zip": "23803", "state": "VA" }, 

{  "address": "2618 W Main St", "city": "Richmond", "zip": "23220", "state": "VA" }, 

{  "address": "2618 W Main St", "city": "Richmond", "zip": "23220", "state": "VA" }, 

{  "address": "2618 Idlewood Ave", "city": "Richmond", "zip": "23220", "state": "VA" }, 

{  "address": "2618 Idlewood Ave", "city": "Richmond", "zip": "23220", "state": "VA" }, 

{  "address": "1837 Grayland Ave", "city": "Richmond", "zip": "23220", "state": "VA" }, 

{  "address": "604 N 32nd St", "city": "Richmond", "zip": "23223", "state": "VA" }, 

{  "address": "604 N 32nd St", "city": "Richmond", "zip": "23223", "state": "VA" }, 

{  "address": "3422 E Broad St", "city": "Richmond", "zip": "23223", "state": "VA" }, 

{  "address": "3422 E Broad St", "city": "Richmond", "zip": "23223", "state": "VA" }, 

{  "address": "301 Dabbs House Rd #APT 377", "city": "Richmond", "zip": "23223", "state": "VA" },

{  "address": "301 Dabbs House Rd #APT 377", "city": "Richmond", "zip": "23223", "state": "VA" }, 

{  "address": "2530 Whitcomb St", "city": "Richmond", "zip": "23223", "state": "VA" }, 

{  "address": "2530 Whitcomb St", "city": "Richmond", "zip": "23223", "state": "VA" }, 

{  "address": "1101 Micheline Ter", "city": "Richmond", "zip": "23223", "state": "VA" },

{  "address": "3254 Broad Rock Blvd", "city": "Richmond", "zip": "23224", "state": "VA" }, 

{  "address": "3254 Broad Rock Blvd", "city": "Richmond", "zip": "23224", "state": "VA" }, 

{  "address": "1885 Fernbrook Dr", "city": "Richmond", "zip": "23224", "state": "VA" }, 

{  "address": "1885 Fernbrook Dr", "city": "Richmond", "zip": "23224", "state": "VA" },

{  "address": "307 Stockton St", "city": "Richmond", "zip": "23224", "state": "VA" }, 

{  "address": "307 Stockton St", "city": "Richmond", "zip": "23224", "state": "VA" }, 

{  "address": "5857 Orcutt Ln", "city": "Richmond", "zip": "23224", "state": "VA" }, 

{  "address": "5857 Orcutt Ln", "city": "Richmond", "zip": "23224", "state": "VA" },

{  "address": "1522 Lone St", "city": "Richmond", "zip": "23224", "state": "VA" },

{  "address": "107 W 34th St", "city": "Richmond", "zip": "23225", "state": "VA" }, 

{  "address": "107 W 34th St", "city": "Richmond", "zip": "23225", "state": "VA" }, 

{  "address": "2303 Bainbridge St", "city": "Richmond", "zip": "23225", "state": "VA" }, 

{  "address": "2303 Bainbridge St", "city": "Richmond", "zip": "23225", "state": "VA" },

{  "address": "1100 German School Rd", "city": "Richmond", "zip": "23225", "state": "VA" }, 

{  "address": "1100 German School Rd", "city": "Richmond", "zip": "23225", "state": "VA" },

{  "address": "6823 Carnation St #D", "city": "Richmond", "zip": "23225", "state": "VA" }, 

{  "address": "6913 Carnation St #B", "city": "Richmond", "zip": "23225", "state": "VA" }, 

{  "address": "440 Westover Hills Blvd", "city": "Richmond", "zip": "23225", "state": "VA" }, 

{  "address": "3464 Colonial M73 Ave", "city": "Roanoke", "zip": "24018", "state": "VA" }, 

{  "address": "3464 Colonial M73 Ave", "city": "Roanoke", "zip": "24018", "state": "VA" }, 

{  "address": "3337 Circle Brook Dr #C", "city": "Roanoke", "zip": "24018", "state": "VA" }, 

{  "address": "3337 Circle Brook Dr #C", "city": "Roanoke", "zip": "24018", "state": "VA" }, 

{  "address": "5105 Canter Dr", "city": "Roanoke", "zip": "24018", "state": "VA" },

{  "address": "5105 Canter Dr", "city": "Roanoke", "zip": "24018", "state": "VA" }, 

{  "address": "3020 Circle Dr SW", "city": "Roanoke", "zip": "24018", "state": "VA" }, 

{  "address": "3020 Circle Dr SW", "city": "Roanoke", "zip": "24018", "state": "VA" }, 

{  "address": "4418 Fontaine Dr", "city": "Roanoke", "zip": "24018", "state": "VA" },

{  "address": "320 Hershberger Rd NW", "city": "Roanoke", "zip": "24012", "state": "VA" }, 

{  "address": "320 Hershberger Rd NW", "city": "Roanoke", "zip": "24012", "state": "VA" }, 

{  "address": "401 Friends Way", "city": "Roanoke", "zip": "24012", "state": "VA" }, 

{  "address": "401 Friends Way", "city": "Roanoke", "zip": "24012", "state": "VA" }, 

{  "address": "501 Mapleton Ave NE", "city": "Roanoke", "zip": "24012", "state": "VA" }, 

{  "address": "501 Mapleton Ave NE", "city": "Roanoke", "zip": "24012", "state": "VA" },

{  "address": "480 Bluebell Ln NW", "city": "Roanoke", "zip": "24012", "state": "VA" }, 

{  "address": "480 Bluebell Ln NW", "city": "Roanoke", "zip": "24012", "state": "VA" }, 

{  "address": "3750 Williamson Rd NE #P", "city": "Roanoke", "zip": "24012", "state": "VA" },

{  "address": "202 Primrose Ln", "city": "Chesapeake", "zip": "23320", "state": "VA" }, 

{  "address": "202 Primrose Ln", "city": "Chesapeake", "zip": "23320", "state": "VA" }, 

{  "address": "609 Shadow Brooke Dr", "city": "Chesapeake", "zip": "23320", "state": "VA" }, 

{  "address": "609 Shadow Brooke Dr", "city": "Chesapeake", "zip": "23320", "state": "VA" }, 

{  "address": "1509 Ring Rd", "city": "Chesapeake", "zip": "23320", "state": "VA" }, 

{  "address": "1509 Ring Rd", "city": "Chesapeake", "zip": "23320", "state": "VA" }, 

{  "address": "717 Sea Pines Run", "city": "Chesapeake", "zip": "23320", "state": "VA" },

{  "address": "717 Sea Pines Run", "city": "Chesapeake", "zip": "23320", "state": "VA" }, 

{  "address": "1811 Beckwood Cmn", "city": "Chesapeake", "zip": "23320", "state": "VA" }, 

{  "address": "3213 Bruin Dr", "city": "Chesapeake", "zip": "23321", "state": "VA" }, 

{  "address": "3213 Bruin Dr", "city": "Chesapeake", "zip": "23321", "state": "VA" }, 

{  "address": "3732 Cannon Point Dr", "city": "Chesapeake", "zip": "23321", "state": "VA" }, 

{  "address": "3732 Cannon Point Dr", "city": "Chesapeake", "zip": "23321", "state": "VA" },

{  "address": "3053 Tyre Neck Rd", "city": "Chesapeake", "zip": "23321", "state": "VA" }, 

{  "address": "3053 Tyre Neck Rd", "city": "Chesapeake", "zip": "23321", "state": "VA" }, 

{  "address": "3209 Meadowbrook Ln", "city": "Chesapeake", "zip": "23321", "state": "VA" },

{  "address": "3209 Meadowbrook Ln", "city": "Chesapeake", "zip": "23321", "state": "VA" }, 

{  "address": "4702 Feldspar Quay", "city": "Chesapeake", "zip": "23321", "state": "VA" }, 

{  "address": "417 Ballahack Rd", "city": "Chesapeake", "zip": "23322", "state": "VA" }, 

{  "address": "417 Ballahack Rd", "city": "Chesapeake", "zip": "23322", "state": "VA" }, 

{  "address": "1108 Kathleen Ln", "city": "Chesapeake", "zip": "23322", "state": "VA" }, 

{  "address": "1108 Kathleen Ln", "city": "Chesapeake", "zip": "23322", "state": "VA" }, 

{  "address": "1502 Hawick Ter", "city": "Chesapeake", "zip": "23322", "state": "VA" },

{  "address": "1502 Hawick Ter", "city": "Chesapeake", "zip": "23322", "state": "VA" }, 

{  "address": "913 Mockingbird Ct", "city": "Chesapeake", "zip": "23322", "state": "VA" }, 

{  "address": "913 Mockingbird Ct", "city": "Chesapeake", "zip": "23322", "state": "VA" },

{  "address": "345 Bartell Dr", "city": "Chesapeake", "zip": "23322", "state": "VA" }, 

{  "address": "1424 Boxwood Dr", "city": "Chesapeake", "zip": "23323", "state": "VA" }, 

{  "address": "1424 Boxwood Dr", "city": "Chesapeake", "zip": "23323", "state": "VA" }, 

{  "address": "3217 Dodd Dr", "city": "Chesapeake", "zip": "23323", "state": "VA" }, 

{  "address": "3217 Dodd Dr", "city": "Chesapeake", "zip": "23323", "state": "VA" }, 

{  "address": "1028 West Rd", "city": "Chesapeake", "zip": "23323", "state": "VA" },

{  "address": "1028 West Rd", "city": "Chesapeake", "zip": "23323", "state": "VA" }, 

{  "address": "1320 Shamrock Garden Rd", "city": "Chesapeake", "zip": "23323", "state": "VA" },

{  "address": "1320 Shamrock Garden Rd", "city": "Chesapeake", "zip": "23323", "state": "VA" },

{  "address": "613 Willow Bend Dr", "city": "Chesapeake", "zip": "23323", "state": "VA" }, 

{  "address": "1 Fernwood Cir", "city": "Hampton", "zip": "23666", "state": "VA" }, 

{  "address": "1 Fernwood Cir", "city": "Hampton", "zip": "23666", "state": "VA" }, 

{  "address": "3 Andros Isle", "city": "Hampton", "zip": "23666", "state": "VA" }, 

{  "address": "3 Andros Isle", "city": "Hampton", "zip": "23666", "state": "VA" },

{  "address": "213 Martha Lee Dr", "city": "Hampton", "zip": "23666", "state": "VA" }, 

{  "address": "213 Martha Lee Dr", "city": "Hampton", "zip": "23666", "state": "VA" }, 

{  "address": "Po Box 7264", "city": "Hampton", "zip": "23666", "state": "VA" }, 

{  "address": "Po Box 7264", "city": "Hampton", "zip": "23666", "state": "VA" }, 

{  "address": "119 Patrician Dr", "city": "Hampton", "zip": "23666", "state": "VA" }, 

{  "address": "105 Priest Ct", "city": "Hampton", "zip": "23669", "state": "VA" }, 

{  "address": "105 Priest Ct", "city": "Hampton", "zip": "23669", "state": "VA" }, 

{  "address": "103 Hamlet Ln", "city": "Hampton", "zip": "23669", "state": "VA" }, 

{  "address": "103 Hamlet Ln", "city": "Hampton", "zip": "23669", "state": "VA" }, 

{  "address": "710 Allendale Dr", "city": "Hampton", "zip": "23669", "state": "VA" }, 

{  "address": "710 Allendale Dr", "city": "Hampton", "zip": "23669", "state": "VA" }, 

{  "address": "23 Royston Dr", "city": "Hampton", "zip": "23669", "state": "VA" }, 

{  "address": "23 Royston Dr", "city": "Hampton", "zip": "23669", "state": "VA" }, 

{  "address": "2 Eaton St", "city": "Hampton", "zip": "23669", "state": "VA" }, 

{  "address": "1613 River Rdg", "city": "Williamsburg", "zip": "23185", "state": "VA" }, 

{  "address": "1613 River Rdg", "city": "Williamsburg", "zip": "23185", "state": "VA" }, 

{  "address": "169 Howard Dr", "city": "Williamsburg", "zip": "23185", "state": "VA" }, 

{  "address": "169 Howard Dr", "city": "Williamsburg", "zip": "23185", "state": "VA" }, 

{  "address": "117 Smokehouse Ln", "city": "Williamsburg", "zip": "23185", "state": "VA" }, 

{  "address": "117 Smokehouse Ln", "city": "Williamsburg", "zip": "23185", "state": "VA" },

{  "address": "103 Southpoint Dr", "city": "Williamsburg", "zip": "23185", "state": "VA" }, 

{  "address": "103 Southpoint Dr", "city": "Williamsburg", "zip": "23185", "state": "VA" }, 

{  "address": "3051 Heritage Landing Rd", "city": "Williamsburg", "zip": "23185", "state": "VA" },

{  "address": "116 Colby Rd", "city": "Williamsburg", "zip": "23188", "state": "VA" },
{  "address": "116 Colby Rd", "city": "Williamsburg", "zip": "23188", "state": "VA" },
{  "address": "116 Theodore Allen Rd", "city": "Williamsburg", "zip": "23188", "state": "VA" },
{  "address": "116 Theodore Allen Rd", "city": "Williamsburg", "zip": "23188", "state": "VA" },
{  "address": "106 Indian Summer Ln", "city": "Williamsburg", "zip": "23188", "state": "VA" },
{  "address": "106 Indian Summer Ln", "city": "Williamsburg", "zip": "23188", "state": "VA" },
{  "address": "104 Astrid Ln", "city": "Williamsburg", "zip": "23188", "state": "VA" },
{  "address": "104 Astrid Ln", "city": "Williamsburg", "zip": "23188", "state": "VA" },
{  "address": "3904 Shady Grove Cir #D", "city": "Williamsburg", "zip": "23188", "state": "VA" },
{  "address": "573 Haystack Landing Rd", "city": "Newport News", "zip": "23602", "state": "VA" },
{  "address": "573 Haystack Landing Rd", "city": "Newport News", "zip": "23602", "state": "VA" },
{  "address": "571 Onancock Trl", "city": "Newport News", "zip": "23602", "state": "VA" },
{  "address": "571 Onancock Trl", "city": "Newport News", "zip": "23602", "state": "VA" },
{  "address": "703 Mac Neil Dr", "city": "Newport News", "zip": "23602", "state": "VA" },
{  "address": "703 Mac Neil Dr", "city": "Newport News", "zip": "23602", "state": "VA" },
{  "address": "852 Holbrook Dr", "city": "Newport News", "zip": "23602", "state": "VA" },
{  "address": "852 Holbrook Dr", "city": "Newport News", "zip": "23602", "state": "VA" },
{  "address": "557 York River Ln", "city": "Newport News", "zip": "23602", "state": "VA" },
{  "address": "67 Stanley Dr", "city": "Newport News", "zip": "23608", "state": "VA" },
{  "address": "67 Stanley Dr", "city": "Newport News", "zip": "23608", "state": "VA" },
{  "address": "477 Reddick Rd", "city": "Newport News", "zip": "23608", "state": "VA" },
{  "address": "477 Reddick Rd", "city": "Newport News", "zip": "23608", "state": "VA" },
{  "address": "220 Crane Cir #APT L", "city": "Newport News", "zip": "23608", "state": "VA" },
{  "address": "220 Crane Cir #APT L", "city": "Newport News", "zip": "23608", "state": "VA" },
{  "address": "1425 Ventura Way", "city": "Newport News", "zip": "23608", "state": "VA" },
{  "address": "1425 Ventura Way", "city": "Newport News", "zip": "23608", "state": "VA" },
{  "address": "460 Richneck Rd", "city": "Newport News", "zip": "23608", "state": "VA" },
{  "address": "2307 Norcova Ave", "city": "Norfolk", "zip": "23513", "state": "VA" },
{  "address": "1340 Longdale Dr", "city": "Norfolk", "zip": "23513", "state": "VA" },
{  "address": "6347 Chesapeake Blvd #APT 56", "city": "Norfolk", "zip": "23513", "state": "VA" },
{  "address": "2305 Alder St", "city": "Norfolk", "zip": "23513", "state": "VA" },
{  "address": "1068 Bland St", "city": "Norfolk", "zip": "23513", "state": "VA" },
{  "address": "1218 Underwood Ave", "city": "Norfolk", "zip": "23513", "state": "VA" },
{  "address": "6912 Bonnot Dr", "city": "Norfolk", "zip": "23513", "state": "VA" },
{  "address": "6337 Sedgefield Dr", "city": "Norfolk", "zip": "23513", "state": "VA" },
{  "address": "901 Spaulding Dr", "city": "Norfolk", "zip": "23513", "state": "VA" },
{  "address": "8139 Pace Rd", "city": "Norfolk", "zip": "23518", "state": "VA" },
{  "address": "8219 Carrene Dr", "city": "Norfolk", "zip": "23518", "state": "VA" },
{  "address": "6438 Bridle Way", "city": "Norfolk", "zip": "23518", "state": "VA" },
{  "address": "1601 Harmon St", "city": "Norfolk", "zip": "23518", "state": "VA" },
{  "address": "929 Mildred St", "city": "Norfolk", "zip": "23518", "state": "VA" },
{  "address": "7854 Azalea Grdn Rd #77", "city": "Norfolk", "zip": "23518", "state": "VA" },
{  "address": "7921 Lion Ave", "city": "Norfolk", "zip": "23518", "state": "VA" },
{  "address": "8036 Danbury Dr", "city": "Norfolk", "zip": "23518", "state": "VA" },
{  "address": "8329 Norristown Dr", "city": "Norfolk", "zip": "23518", "state": "VA" },
{  "address": "4384 Lake Prince Dr", "city": "Suffolk", "zip": "23434", "state": "VA" },
{  "address": "4384 Lake Prince Dr", "city": "Suffolk", "zip": "23434", "state": "VA" },
{  "address": "1073 Carolina Rd", "city": "Suffolk", "zip": "23434", "state": "VA" },
{  "address": "1073 Carolina Rd", "city": "Suffolk", "zip": "23434", "state": "VA" },
{  "address": "1161 Nansemond Pky", "city": "Suffolk", "zip": "23434", "state": "VA" },
{  "address": "1161 Nansemond Pky", "city": "Suffolk", "zip": "23434", "state": "VA" },
{  "address": "910 Brook Ave", "city": "Suffolk", "zip": "23434", "state": "VA" },
{  "address": "910 Brook Ave", "city": "Suffolk", "zip": "23434", "state": "VA" },
{  "address": "219 Prospect Rd #APT 120", "city": "Suffolk", "zip": "23434", "state": "VA" },
{  "address": "2632 N Nansemond Dr", "city": "Suffolk", "zip": "23435", "state": "VA" },
{  "address": "2632 N Nansemond Dr", "city": "Suffolk", "zip": "23435", "state": "VA" },
{  "address": "5106 W Creek Ct", "city": "Suffolk", "zip": "23435", "state": "VA" },
{  "address": "5106 W Creek Ct", "city": "Suffolk", "zip": "23435", "state": "VA" },
{  "address": "3915 Breezeport Way", "city": "Suffolk", "zip": "23435", "state": "VA" },
{  "address": "3915 Breezeport Way", "city": "Suffolk", "zip": "23435", "state": "VA" },
{  "address": "5218 Shoal Creek Rd", "city": "Suffolk", "zip": "23435", "state": "VA" },
{  "address": "5218 Shoal Creek Rd", "city": "Suffolk", "zip": "23435", "state": "VA" },
{  "address": "1050 Belle Orchard Ln", "city": "Suffolk", "zip": "23435", "state": "VA" },
{  "address": "3100 Shore Dr #APT 302", "city": "Virginia Beach", "zip": "23451", "state": "VA" },
{  "address": "3100 Shore Dr #APT 302", "city": "Virginia Beach", "zip": "23451", "state": "VA" },
{  "address": "2300 Beach Haven Dr #301", "city": "Virginia Beach", "zip": "23451", "state": "VA" },
{  "address": "2300 Beach Haven Dr #301", "city": "Virginia Beach", "zip": "23451", "state": "VA" },
{  "address": "522 Pine Song Ln", "city": "Virginia Beach", "zip": "23451", "state": "VA" },
{  "address": "522 Pine Song Ln", "city": "Virginia Beach", "zip": "23451", "state": "VA" },
{  "address": "417 Terrace Ave", "city": "Virginia Beach", "zip": "23451", "state": "VA" },
{  "address": "417 Terrace Ave", "city": "Virginia Beach", "zip": "23451", "state": "VA" },
{  "address": "105 Shore View Ct", "city": "Virginia Beach", "zip": "23451", "state": "VA" },
{  "address": "3604 Malibu Palms Dr #APT 102", "city": "Virginia Beach", "zip": "23452", "state": "VA" },
{  "address": "3604 Malibu Palms Dr #APT 102", "city": "Virginia Beach", "zip": "23452", "state": "VA" },
{  "address": "206 N Fir Ave", "city": "Virginia Beach", "zip": "23452", "state": "VA" },
{  "address": "206 N Fir Ave", "city": "Virginia Beach", "zip": "23452", "state": "VA" },
{  "address": "1308 W Little Neck Rd", "city": "Virginia Beach", "zip": "23452", "state": "VA" },
{  "address": "1308 W Little Neck Rd", "city": "Virginia Beach", "zip": "23452", "state": "VA" },
{  "address": "929 Woodmark Ct", "city": "Virginia Beach", "zip": "23452", "state": "VA" },
{  "address": "929 Woodmark Ct", "city": "Virginia Beach", "zip": "23452", "state": "VA" },
{  "address": "241 S Budding Ave", "city": "Virginia Beach", "zip": "23452", "state": "VA" },
{  "address": "2821 Augusta Cir", "city": "Virginia Beach", "zip": "23453", "state": "VA" },
{  "address": "2821 Augusta Cir", "city": "Virginia Beach", "zip": "23453", "state": "VA" },
{  "address": "3960 Rica Dr", "city": "Virginia Beach", "zip": "23453", "state": "VA" },
{  "address": "3960 Rica Dr", "city": "Virginia Beach", "zip": "23453", "state": "VA" },
{  "address": "3812 Keelboat Cir", "city": "Virginia Beach", "zip": "23453", "state": "VA" },
{  "address": "3244 Twinflower Ln", "city": "Virginia Beach", "zip": "23453", "state": "VA" },
{  "address": "2933 Dante Pl", "city": "Virginia Beach", "zip": "23453", "state": "VA" },
{  "address": "1232 Green Cedar Ln", "city": "Virginia Beach", "zip": "23453", "state": "VA" },
{  "address": "913 Roberval Dr", "city": "Virginia Beach", "zip": "23454", "state": "VA" },
{  "address": "913 Roberval Dr", "city": "Virginia Beach", "zip": "23454", "state": "VA" },
{  "address": "1537 Mill Dam Rd", "city": "Virginia Beach", "zip": "23454", "state": "VA" },
{  "address": "1537 Mill Dam Rd", "city": "Virginia Beach", "zip": "23454", "state": "VA" },
{  "address": "1710 Sword Dancer Dr", "city": "Virginia Beach", "zip": "23454", "state": "VA" },
{  "address": "1710 Sword Dancer Dr", "city": "Virginia Beach", "zip": "23454", "state": "VA" },
{  "address": "2142 Retreat Ct", "city": "Virginia Beach", "zip": "23454", "state": "VA" },
{  "address": "2142 Retreat Ct", "city": "Virginia Beach", "zip": "23454", "state": "VA" },
{  "address": "1221 Gunn Hall Dr", "city": "Virginia Beach", "zip": "23454", "state": "VA" },
{  "address": "4948 Casablanca Rd", "city": "Virginia Beach", "zip": "23455", "state": "VA" },
{  "address": "4948 Casablanca Rd", "city": "Virginia Beach", "zip": "23455", "state": "VA" },
{  "address": "5513 Westbury Rd", "city": "Virginia Beach", "zip": "23455", "state": "VA" },
{  "address": "5513 Westbury Rd", "city": "Virginia Beach", "zip": "23455", "state": "VA" },
{  "address": "5001 Coltfield Ct", "city": "Virginia Beach", "zip": "23455", "state": "VA" },
{  "address": "5001 Coltfield Ct", "city": "Virginia Beach", "zip": "23455", "state": "VA" },
{  "address": "1037 Dulcie Ave", "city": "Virginia Beach", "zip": "23455", "state": "VA" },
{  "address": "1037 Dulcie Ave", "city": "Virginia Beach", "zip": "23455", "state": "VA" },
{  "address": "4424 Chandler Ln", "city": "Virginia Beach", "zip": "23455", "state": "VA" }
]


# It returns the date formatted as YYYYMMDD to be used in the output's file name
def get_date():
	d = str(datetime.date.today())
	s = d.replace('-', '')
	return s

def save_to_file(data):
	date = get_date()
	new_path = os.path.join(os.getcwd(), f'PD_Issuer1_{date}_VA.json')
	print(new_path)
	with open(new_path, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=4)
	print(f'Data generated into this file: PD_Issuer1_{date}_VA.json')

def generate_data(addresses):
    data = []
    for address in addresses:
        address_object =  {
            "address1": f'{address["address"].strip()}',
            "address2": "",
            "city": f"{address['city']}",
            "state": f"VA",
            "postalCode": f"{address['zip']}",
            "coordinates": {
                "lat": 0,
                "lng": 0
            }
        }    
        data.append(address_object)
    save_to_file(data)
    
# we call the function to process the addresses list
generate_data(addresses_list)
