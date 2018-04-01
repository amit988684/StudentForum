#include <iostream>
#include <cstdio>
#include <string.h>
#include <fstream>
using namespace std;

int Heap_size=0;
int Heap_length=0;
int huff_man[130];
string code_huff[130];

typedef struct HUFF_NODES{
	char data;
	int freq;
	HUFF_NODES* left,*right;
}HUFF_NODES;

typedef struct MIN_NODE{
	int freq;
	HUFF_NODES *address;
}MIN_NODE;

//Fuction Prototype
HUFF_NODES* CREATENODE( char data, int freq );
void BUILD_MINHEAP(int *arr,HUFF_NODES **nodes);
void MIN_HEAPIFY(int *arr,HUFF_NODES** nodes, int i);
MIN_NODE  HEAP_EXTRACT_MIN(int *arr,HUFF_NODES **nodes);
void INSERT_MIN_HEAP(int *arr,HUFF_NODES **nodes,int freq,HUFF_NODES *insert);
HUFF_NODES* BUILD_HUFFMAN_TREE( int *arr , char *character);
void printCode(int code[],int top, char)	;
void print_encodes(FILE *fp,HUFF_NODES *root, int code[], int top);
//End of Function prototype

HUFF_NODES* CREATENODE( char data, int freq )
{
	HUFF_NODES *temp= new HUFF_NODES();
	temp->data=data;
	temp->freq=freq;
	temp->left=temp->right=NULL;
	return temp;
}

char* file_name_generator(const char *name1)
{
	//Location of folder
	char file_name[100]="";
	//Dynamic allocation
	char *file_name1=(char *)malloc(100*sizeof(char));
	//Required procedure for appending the file name to path
	strcpy(file_name1,file_name);
	strcat(file_name1,name1);
	return file_name1;
}

void BUILD_MINHEAP(int *arr,HUFF_NODES **nodes)
{
	Heap_size=Heap_length;
	for (int i = (Heap_size-1)/2 ; i >=0 ; --i)
	{
		MIN_HEAPIFY(arr,nodes,i);
	}
}

void MIN_HEAPIFY(int *arr,HUFF_NODES** nodes, int i)
{
	int smallest=i;
	int l=2*i+1;
	int r=2*i+2;

	if( l<= Heap_size && arr[l] < arr[i] )
		smallest=l;

	if( r<=Heap_size && arr[r]<arr[smallest])
		smallest=r;

	if( smallest != i )
	{
		int temporary=arr[i];
		arr[i]=arr[smallest];
		arr[smallest]=temporary;

		HUFF_NODES* temp=nodes[i];
		nodes[i]=nodes[smallest];
		nodes[smallest]=temp;

		MIN_HEAPIFY(arr,nodes,smallest);
	}

}

MIN_NODE  HEAP_EXTRACT_MIN(int *arr,HUFF_NODES **nodes)
{
	MIN_NODE a;
	a.freq=0;
	a.address=NULL;

	if(Heap_size < 0)
		cout<<"Heap Underflow!"<<endl;
	else
	{
		a.freq=arr[0];
		a.address=nodes[0];

		arr[0]=arr[Heap_size];
		nodes[0]=nodes[Heap_size];

		Heap_size-=1;

		MIN_HEAPIFY(arr,nodes,0);
	}
	return a;
}

void INSERT_MIN_HEAP(int *arr,HUFF_NODES **nodes,int freq,HUFF_NODES *insert)
{
	Heap_size+=1;
	arr[Heap_size]=freq;
	nodes[Heap_size]=insert;

	int i=Heap_size;
	while( i >= 0 && arr[(i-1)/2] > arr[i])
	{
		int k=(i-1)/2;
		int temporary=arr[k];
		arr[k]=arr[i];
		arr[i]=temporary;

		HUFF_NODES* temp=nodes[k];
		nodes[k]=nodes[i];
		nodes[i]=temp;

		i=(i-1)/2;	
	}
	
}

HUFF_NODES* BUILD_HUFFMAN_TREE( int *arr , char *character)
{
	HUFF_NODES *nodes[Heap_length];
	for(int i=0;i<=Heap_length;i++)
		nodes[i]=CREATENODE(character[i],arr[i]);


	BUILD_MINHEAP(arr,nodes);

	while(Heap_size >= 1)
	{
		MIN_NODE a,b;

		a=HEAP_EXTRACT_MIN(arr,nodes);
		b=HEAP_EXTRACT_MIN(arr,nodes);

		int comb_freq= a.freq + b.freq;
		char ch='$';
		HUFF_NODES* temp=CREATENODE(ch,comb_freq);

		temp->left=a.address;
		temp->right=b.address;

		INSERT_MIN_HEAP(arr,nodes,comb_freq,temp);
	}
	return nodes[0];
}
void printCode(FILE *fp,int code[],int top,char cc)
{
	huff_man[cc]++;
	string a="";
	for(int i=0;i<top;i++)
			a=a+(char)(code[i]+48);
	cout<<a;
	const char *s=a.c_str();
	fprintf(fp,"%s\n",s);
	code_huff[cc]=a;
	cout<<endl;
}

void print_encodes(FILE *fp,HUFF_NODES *root, int code[], int top)
{
	if(root->left)
	{
		code[top]=0;
		print_encodes(fp,root->left,code,top+1);
	}
	if (root->right)
	{
        code[top] = 1;
        print_encodes(fp,root->right,code,top+1);
    }
	if (!(root->left) && !(root->right)) 
	{
		cout<<root->data<<": ";
		fprintf(fp, "%c ",root->data);
	    printCode(fp,code, top,root->data);
	}  	
}

 int calcFreq(string str, int size,char *character,int *arr)
 {
    int freq[200]={0};
	int k=0;

     for (int i=0; i<size ; i++)
         	freq[(int)str[i]]+=1;
    for (int i = 32; i < 130; ++i)
    {
    	if( freq[i] !=0 )
    	{
    		character[k]=(char)i;
    		arr[k]=freq[i];
    		k++;
    	}
    }
     return k-1;
 }

 void DECODE(HUFF_NODES *root,string dec,int size)
{
	HUFF_NODES *temp=root;
	int i=0;
	while(i<size)
	{
		if(dec[i]=='0' && temp->left)
			temp=temp->left;
	    if(dec[i]=='1' && temp->right)
			temp=temp->right;
		if(!(temp->left) && !(temp->right))
		{
			cout<<temp->data;
			temp=root;
		}
		i++;
	}
	cout<<endl;
}


int main()
{
	char *filename,filee[50];

	printf("Enter the file name?\n");
	scanf("%s",filee);

	filename=file_name_generator(filee);

	FILE *fp_t=fopen(filename,"r");

	if ( fp_t == NULL )
	{
		puts ( "Cannot open file" ) ;
		exit(0) ;
	}

	string str="";
	char dummy=' ';
	while (fscanf (fp_t,"%c",&dummy) != EOF )
		str+=dummy;

	int size=str.length();
	cout<<size<<endl;
	char character[size];
	int arr[size]={0};
	
	Heap_length=calcFreq(str,size,character,arr);
	
	int code[Heap_length]={0};

	cout << "Alphabet"<<"	"<<"Frequency"<<endl;
	for (int i = 0; i <= Heap_length; ++i)
	{
		cout<<character[i]<<"		"<<arr[i]<<endl;
	}

	HUFF_NODES *root=BUILD_HUFFMAN_TREE(arr,character);

	cout<<"Encodes are:"<<endl;
	FILE *fp=fopen("HUFFMAN_TREE.txt","w");
	print_encodes(fp,root,code,0);
	cout<<"**************************"<<endl;
	fclose(fp);
	fclose(fp_t);

	// for (int i = 0; i < 130; ++i)
	// {
	// 	if(huff_man[i] != 0)
	// 	{
	// 		cout<<(char)i<<" "<<code_huff[i]<<endl;
	// 	}
	// }

	string new_encode="";
	
	for(int i=0;i<str.length();i++)
	{
		if(huff_man[str[i]] != 0)
		{
			new_encode+=code_huff[str[i]];
		}
	}
	// cout<<new_encode;

	ofstream name ("encode.txt");
	name<<new_encode;
	name.close();

	//  while (fscanf (fp_t,"%c",&dummy) != EOF )
	//  {
	// 	while(fscanf (fp,"%c",&ccc) != EOF )
	//  	{
	// 		printf("%c \n",ccc);
	// 		if(dummy == ccc){
				
	// 			while(fscanf (fp,"%c",&ccc) != EOF )
	// 			{
	// 				if(ccc == 13)

	return 0;
}