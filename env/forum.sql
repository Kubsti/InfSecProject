CREATE Table Forumuser(
randuserid text not null,
username text not null,
passwordhash text not null,
PRIMARY KEY (randuserid)
);

CREATE TABLE Posts(
postid BIGINT,
postcontent text not null,
posttitel text not null,
PRIMARY KEY (postid)
);

CREATE TABLE Comments(
commentid BIGINT,
commentcontent text not null,
PRIMARY KEY (commentid)
);

CREATE TABLE Hasposts(
userid text not null REFERENCES Forumuser(randuserid),
postid BIGINT not null REFERENCES Posts(postid),
UNIQUE(postid)
);

CREATE TABLE hascomments(
postid BIGINT not null REFERENCES Posts(postid),
comentid BIGINT not null REFERENCES Comments(commentid)
);