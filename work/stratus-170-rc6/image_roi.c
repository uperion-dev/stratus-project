#include <ApplicationServices/ApplicationServices.h>
#include <ImageIO/ImageIO.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char**argv){for(int f=1;f<argc;f++){CFURLRef u=CFURLCreateFromFileSystemRepresentation(0,(unsigned char*)argv[f],strlen(argv[f]),0);CGImageSourceRef s=CGImageSourceCreateWithURL(u,0);CGImageRef im=CGImageSourceCreateImageAtIndex(s,0,0);size_t w=CGImageGetWidth(im),h=CGImageGetHeight(im);unsigned char*d=calloc(w*h,4);CGColorSpaceRef cs=CGColorSpaceCreateDeviceRGB();CGContextRef c=CGBitmapContextCreate(d,w,h,8,w*4,cs,kCGImageAlphaPremultipliedLast);CGContextDrawImage(c,CGRectMake(0,0,w,h),im);printf("%s",argv[f]);for(int region=0;region<4;region++){int r=region==0?16:region==1?24:region==2?40:64;double sum=0;int count=0,max=0;for(int y=337-r;y<337+r;y++)for(int x=720-r;x<720+r;x++){if(region>0&&abs(x-720)<r/2&&abs(y-337)<r/2)continue;for(int k=0;k<3;k++){int v=d[(y*w+x)*4+k];sum+=v;count++;if(v>max)max=v;}}printf(" ROI%d_mean=%.8f max=%d",r,sum/count,max);}puts("");free(d);CGContextRelease(c);CGColorSpaceRelease(cs);CGImageRelease(im);CFRelease(s);CFRelease(u);}return 0;}
