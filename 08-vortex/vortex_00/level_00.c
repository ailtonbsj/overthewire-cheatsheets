#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>

#define HOST "vortex.labs.overthewire.org"
#define PORT 5842

void request(int sockfd)
{
	char response[4][4];
	bzero(response, sizeof(response));
	read(sockfd, response[0], 4);
	read(sockfd, response[1], 4);
	read(sockfd, response[2], 4);
	read(sockfd, response[3], 4);

	struct bytes
	{
		unsigned int a, b, c, d;
	} *x = (struct bytes *)&response;
	unsigned int sum = x->a + x->b + x->c + x->d;
	write(sockfd, &sum, 4);

	char buff[100];
	bzero(buff, sizeof(buff));
	read(sockfd, buff, sizeof(buff));
	printf("%s\n", buff);
}

int resolveHost(char *hostname, char *ip);

int main()
{
	char ip[16];
	resolveHost(HOST, ip);
	printf("Connecting %s:%d ...\n", ip, PORT);

	int sockfd;
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd == -1)
	{
		printf("Socket creation failed...\n");
		exit(1);
	}

	struct sockaddr_in servAddr;
	servAddr.sin_family = AF_INET;
	servAddr.sin_addr.s_addr = inet_addr(ip);
	servAddr.sin_port = htons(PORT);
	if (connect(sockfd, (struct sockaddr *)&servAddr, sizeof(servAddr)) != 0)
	{
		printf("Connection with the server failed...\n");
		exit(1);
	}
	request(sockfd);
	close(sockfd);
}

int resolveHost(char *hostname, char *ip)
{
	struct hostent *host;
	struct in_addr **addrList;
	int i;
	if ((host = gethostbyname(hostname)) == NULL)
	{
		herror("gethostbyname error");
		return 1;
	}
	addrList = (struct in_addr **)host->h_addr_list;
	for (i = 0; addrList[i] != NULL; i++)
	{
		strcpy(ip, inet_ntoa(*addrList[i]));
		return 0;
	}
	return 1;
}