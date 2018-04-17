#include<iostream>
#include<vector>
using namespace std;

typedef struct packet {
  int source;
  int dest;
  int hop;
  int seq;
  int sender;
}packet;

typedef struct Node {
  int id;
  int sequence;
  vector<int> neigh;
  vector<packet> p;
}node;


packet createPacket(int src,int dst,int hop,int seq) {
  packet p;
  p.source = src;
  p.dest = dst;
  p.hop = hop;
  p.seq = seq;
  p.sender = src;
  return p;
}


void sendPackets(packet p,node nodes[],vector<int> v,int sender,int newhop) {
  if(sender == p.dest-1) {
    nodes[p.dest-1].sequence = p.seq;
    return ;
  }
  p.hop = newhop;
  p.sender = sender+1;
  for(vector<int>::iterator it = v.begin();it!=v.end();it++) {
    if(*it!=nodes[sender].p[0].sender) {
      nodes[*it-1].p.push_back(p);
      cout<<"Packet Sent From "<<sender+1<<" To "<<*it<<" With Hop Count "<< p.hop;
      if(*it==p.dest)
	cout<<" ----> Reached Destination Node "<<*it<<endl;
      else
	cout<<endl;
    }
  }

}

int main() {
    int n,i,j,src,dst;
    n = 5;
    cout<<"Enter The Number Of Nodes:";
    //cin>>n;
    //int r[n][n];
    int r[][5] = {{0,1,1,1,0},{1,0,0,0,1},{1,0,0,1,1},{1,0,1,0,1},{0,1,1,1,0}};
    //node *nodes =  new node[(sizeof(node)*n)];
    cout<<"Enter The Adjacency Matrix.."<<endl;
    node nodes[n];
    for(i=0;i<n;i++) {
      cout<<"Node "<<i+1<<":";
        nodes[i].id = i+1;
	nodes[i].sequence = 0;
        for(j=0;j<n;j++) {
	  //cin>>r[i][j];
            if(r[i][j]==1)
            nodes[i].neigh.push_back(j+1);
        }
    }
    cout<<"Enter Source And Destination :";
    cin>>src>>dst;
    //src = 1;
    //dst = 5;
    
    packet p = createPacket(src,dst,3,20);
    int age = p.hop;
    nodes[src-1].p.push_back(p);
    sendPackets(p,nodes,nodes[src-1].neigh,src-1,age);
    nodes[src-1].sequence = p.seq;
    nodes[src-1].p.erase(nodes[src-1].p.begin());
    
    while(age!=1) {
      for(i=0;i<n;i++) 
	if(nodes[i].sequence != p.seq && nodes[i].p.size() > 0 && nodes[i].p[0].hop == age ) {	  
	  sendPackets(p,nodes,nodes[i].neigh,i,age-1);
	  nodes[i].sequence = p.seq;
	  nodes[i].p.erase(nodes[i].p.begin());
	}
      age--;
    }
          
}

