

CREATE TABLE IF NOT EXISTS `douyu_link` (
  
`id` varchar(30) DEFAULT NULL,
  
`title` varchar(50) DEFAULT NULL,
  
`js` int(10) DEFAULT NULL,
 
`game` varchar(15) DEFAULT NULL,
  
`link` text,
  
`time` datetime DEFAULT NULL
) 
ENGINE=MyISAM DEFAULT CHARSET=utf8;




CREATE TABLE IF NOT EXISTS `huya_link` (
  
`id` varchar(30) DEFAULT NULL,
  
`title` varchar(50) DEFAULT NULL,
  
`js` int(10) DEFAULT NULL,
 
`game` varchar(15) DEFAULT NULL,
  
`link` text,
  
`time` datetime DEFAULT NULL
) 
ENGINE=MyISAM DEFAULT CHARSET=utf8;





CREATE TABLE IF NOT EXISTS `huya_zhubo` (
  
`id` varchar(30) DEFAULT NULL,
  
`title` varchar(50) DEFAULT NULL,
  
`count` int(10) DEFAULT NULL,
 
`game` varchar(15) DEFAULT NULL,
  
`link` text,
  
`time` datetime DEFAULT NULL
) 
ENGINE=MyISAM DEFAULT CHARSET=utf8;

